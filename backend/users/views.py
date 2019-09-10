import json
from rest_framework_jwt.settings import api_settings
from django_redis import get_redis_connection
from .models import UserInfo
from django.core.mail import send_mail

from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse,JsonResponse,HttpResponseBadRequest
from utils.captcha.captcha import Captcha

from django.conf import settings



# Create your views here.

class Regiter(View):
    def get(self, request, uuid):
        captcha = Captcha()
        text, image = captcha.generate_captcha()
        # 连接redis数据库，写入验证码,UUID
        redis = get_redis_connection('verify')
        redis.setex('uuid:%s' % uuid, 300, text)
        return HttpResponse(image, content_type="image/jpg")

    def post(self,request):
        json_str = request.body.decode()
        data = json.loads(json_str)
        print(data)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        uuid = data.get('uuid')
        captcha = data.get('captcha')
        redis = get_redis_connection('verify')
        text = redis.get('uuid:%s' % uuid)
        if not text:
            print('不存在')
            return HttpResponseBadRequest({'msg': '验证码已过期'})
        text = text.decode()
        if text.upper() != captcha.upper():
            print(text, captcha)
            return HttpResponseBadRequest({'msg': '验证码不匹配'})
        print('ok')

        user_exist = UserInfo.objects.filter(username=username).exists()
        if user_exist:
            print('用户名已存在')
            return HttpResponseBadRequest({'msg': '用户名已存在'})

        print(username)
        print(password)
        print(email)
        if not all([username,password,email]):
            print('信息不完整')
            return HttpResponseBadRequest({'msg': '信息不完整'})

        user = UserInfo(
            username=username,
            password=password,
            email=email
        )
        user.save()
        user_id = user.id
        print(user_id, 'user_id')

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return JsonResponse({'username':username,'user_id':user_id,'token':token,'msg':'successful'})


class Login(View):
    def get(self, request, uuid):
        captcha = Captcha()
        text, image = captcha.generate_captcha()
        # 连接redis数据库，写入验证码,UUID
        redis = get_redis_connection('verify')
        redis.setex('uuid:%s' % uuid, 300, text)
        print("已写入redis")
        return HttpResponse(image, content_type="image/jpg")

    def post(self, request):
        json_str = request.body.decode()
        data = json.loads(json_str)
        username = data.get('username')
        password = data.get('password')
        captcha = data.get('captcha')
        uuid = data.get('uuid')

        try:
            user = UserInfo.objects.get(username=username)
            if user.password == password:
                print("密码正确")
            else:
                print("密码 不正确")
                return HttpResponseBadRequest({'msg': '密码错误'})
        except:
            print("用户不存在")
            return HttpResponseBadRequest({'msg': '用户不存在'})

        redis = get_redis_connection('verify')
        text = redis.get('uuid:%s' % uuid)
        if not text:
            print('不存在')
            return HttpResponseBadRequest({'msg': '验证码已过期'})
        text = text.decode()
        if text.upper() != captcha.upper():
            print(text, captcha)
            return HttpResponseBadRequest({'msg': '验证码不匹配'})

        print('ok')

        user_id = user.id

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return JsonResponse({'username': username, 'user_id': user_id, 'token': token, 'msg': 'successful'})


class Forgot(View):
    def get(self, *args):
        try:
            request = args[0]
            uuid = args[1]
            email = args[2]
        except:
            return HttpResponseBadRequest
        captcha = Captcha()
        text = captcha.generate_captcha(flag="text")
        text = "".join(text)
        # redis数据库写入
        redis = get_redis_connection('email')
        redis.setex('uuid:%s' % uuid, 300, text)
        print(text)

        # 发送邮件
        try:
            send_mail('YesLab教务系统密码重置', '验证码：'+text, settings.EMAIL_HOST_USER, [email], fail_silently=False)
            stat = 'true'
        except:
            stat = 'false'
        print(stat)
        return HttpResponse(stat)

    def post(self, request):
        json_str = request.body.decode()
        data = json.loads(json_str)
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')
        captcha = data.get('captcha')
        uuid = data.get('uuid')

        # 对输入信息进行判断
        try:
            user = UserInfo.objects.get(username=username, email=email)
        except:
            print("用户不存在")
            return HttpResponseBadRequest({'msg': '用户不存在或邮箱错误！'})
        redis = get_redis_connection('email')
        text = redis.get('uuid:%s' % uuid)
        print(uuid)
        if not text:
            print('不存在')
            return HttpResponseBadRequest({'msg': '验证码已过期'})
        text = text.decode()
        if text.upper() != captcha.upper():
            print(text, captcha)
            return HttpResponseBadRequest({'msg': '验证码错误'})
        if user.password == password:
            print("密码不能与旧密码相同")
            return HttpResponseBadRequest({'msg': '密码不能与旧密码相同'})

        # 修改密码
        user.password = password
        user.save()

        user_id = user.id
        return JsonResponse({'username': username, 'user_id': user_id, 'msg': 'successful'})
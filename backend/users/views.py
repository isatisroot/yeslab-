import json
from rest_framework_jwt.settings import api_settings
from django_redis import get_redis_connection
from .models import UserInfo

from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse,JsonResponse,HttpResponseBadRequest
from utils.captcha.captcha import Captcha


# Create your views here.

class Regiter(View):
    def get(self,request,uuid):
        captcha = Captcha()
        text,image = captcha.generate_captcha()
        # 连接redis数据库，写入验证码,UUID
        redis = get_redis_connection('verify')
        redis.setex('uuid:%s'% uuid,300,text)
        return HttpResponse(image,content_type="image/jpg")

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
            return HttpResponseBadRequest({'msg':'验证码已过期'})
        text = text.decode()
        if text.upper() != captcha.upper():
            print(text,captcha)
            return HttpResponseBadRequest({'msg':'验证码不匹配'})
        print('ok')

        user_exist = UserInfo.objects.filter(username=username).exists()
        if user_exist:
            print('用户名已存在')
            return HttpResponseBadRequest({'msg':'用户名已存在'})

        print(username)
        print(password)
        print(email)
        if not all([username,password,email]):
            print('信息不完整')
            return HttpResponseBadRequest({'msg':'信息不完整'})

        user = UserInfo(
            username=username,
            password=password,
            email=email
        )
        user.save()
        user_id = user.id
        print(user_id,'user_id')

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return JsonResponse({'username':username,'user_id':user_id,'token':token,'msg':'successful'})
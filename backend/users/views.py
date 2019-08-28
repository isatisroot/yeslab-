from django.shortcuts import render
from django.views.generic import View
from django.http.response import HttpResponse,JsonResponse
from django_redis import get_redis_connection
from utils.captcha.captcha import Captcha
import json
# Create your views here.

class Regiter(View):
    def get(self,request,uuid):
        print(uuid)
        captcha = Captcha()
        text,image = captcha.generate_captcha()
        redis = get_redis_connection('verify')
        redis.setex('uuid:%s'% uuid,300,text)
        return HttpResponse(image,content_type="image/jpg")

    def post(self,request):
        json_str = request.body.decode()
        data = json.loads(json_str)
        print(data)
        username = data.get('username')
        uuid = data.get('uuid')
        captcha = data.get('captcha')
        redis = get_redis_connection('verify')
        text = redis.get('uuid:%s' % uuid)
        print(text)
        if not text:
            print('不存在')
            return HttpResponse({'msg':'验证码已过期'},status=301)
        text = text.decode()
        if text.upper() != captcha.upper():
            print(text,captcha)
            return HttpResponse({'msg':'验证码不匹配'})
        print('ok')
        return JsonResponse({'username':username,'user_id':1,'token':'aaaaaa','msg':'successful'})
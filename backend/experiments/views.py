import requests
from django.views import View
from django.http.response import JsonResponse
# Create your views here.
class Experiment(View):
    def get(self,request):
        url = "http://183.6.116.44:18080/remote/api/tokens"
        user_info = {"username": "guacadmin", "password": "guacadmin"}
        res = requests.post(url, data=user_info)

        print(res)
        token_lab = ''

        return JsonResponse({})


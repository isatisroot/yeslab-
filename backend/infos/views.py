import datetime
import time
from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse,JsonResponse
from .models import ReservationInfo
from utils.constant import TIME_BUKET
# Create your views here.

class Reservation(View):
    def get(self,request):
        dataList = []
        req_date = request.GET.get('date')

        try:
            query = ReservationInfo.objects.filter(date=req_date)
        except Exception as e:
            print(e)
        else:

            for q in query:
                print(datetime.datetime.strftime(q.date,'%Y-%m-%d'))
                data = {
                    # 'date':datetime.datetime.strftime(q.date,'%Y-%m-%d'),
                    'userid':q.user_id,
                    'tb_id':q.tb_id,
                    'time_bucket':TIME_BUKET[q.tb_id]
                }
                dataList.append(data)
        print(dataList)
        return JsonResponse(dataList, safe=False)

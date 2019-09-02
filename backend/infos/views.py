import datetime
from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse,JsonResponse
from .models import ReservationInfo
# Create your views here.

class Reservation(View):
    def get(self,request):
        dataList = []
        date = request.GET.get('date')
        print(date)
        try:
            query = ReservationInfo.objects.filter(date=date)
        except Exception as e:
            print(e)
        else:

            for q in query:
                print(datetime.datetime.strftime(q.date,'%Y-%m-%d'))
                data = {
                    # 'date':datetime.datetime.strftime(q.date,'%Y-%m-%d'),
                    'user_id':q.user_id,
                    'tb_id':q.tb_id,
                    'time_bucket':'0:00-1:00'
                }
                dataList.append(data)
        print(dataList)
        return JsonResponse(dataList, safe=False)

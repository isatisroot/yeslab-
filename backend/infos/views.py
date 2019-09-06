import datetime
import time,json
from django.shortcuts import render
from django.views import View
from django.http.response import HttpResponse,JsonResponse,HttpResponseBadRequest
from .models import ReservationInfo,InterviewInfo
from users.models import UserInfo
from utils.constant import TIME_BUKET,INTERVIEW_TIME_BUKET
from utils.common import time_to_lab
from django.db.models import Count
# Create your views here.

class Reservation(View):
    def make_response(self,query):
        dataList = []
        for q in query:
            data = {
                'date': datetime.datetime.strftime(q.date, '%Y-%m-%d'),

                'userid': q.user_id,
                'tb_id': q.tb_id,
                'time_bucket': TIME_BUKET[q.tb_id]
            }
            dataList.append(data)

        return dataList
    def get(self,request):
        req_date = request.GET.get('date')

        try:
            query = ReservationInfo.objects.filter(date=req_date)
        except Exception as e:
            print(e)
        else:
            dataList = self.make_response(query)

        # print(dataList)
            return JsonResponse(dataList, safe=False)

    def post(self,request):
        json_str = request.body.decode()
        req_data = json.loads(json_str)
        date = req_data.get('date')
        tb_id = req_data.get('tb_id')
        user_id = req_data.get('userid')
        print(date,tb_id,user_id)
        q = ReservationInfo.objects.filter(date=date,tb_id=tb_id)[0]
        if q.user_id:
            return HttpResponseBadRequest(content='已经预约')

        q.user_id = user_id
        q.save()
        print('预约成功')
        query = ReservationInfo.objects.filter(date=date)
        dataList = self.make_response(query)
        print(dataList)
        return JsonResponse(dataList,safe=False)

class InterviewView(View):
    def get(self,request):
        req_date = request.GET.get('date')

        query = InterviewInfo.objects.filter(date=req_date)
        print(query)
        dataList =[]

        for q in query:
            data = {
                'date': datetime.datetime.strftime(q.date, '%Y-%m-%d'),
                'remaining':q.num-q.user.count(),
                'tb_id': q.tb_id,

                'time_bucket': INTERVIEW_TIME_BUKET[q.tb_id]
            }
            dataList.append(data)

        print(dataList)
        return JsonResponse(dataList, safe=False)

    def post(self,request):
        json_str = request.body.decode()
        req_data = json.loads(json_str)
        print(req_data)
        date = req_data.get('date')
        tb_id = req_data.get('tb_id')
        user_id = req_data.get('userid')

        i = InterviewInfo.objects.filter(date=date,tb_id=tb_id)[0]
        count = i.user.count()
        num = i.num
        if count >= num:
            return HttpResponseBadRequest(content='人数已达上限'.encode())

        u = UserInfo.objects.get(id=user_id)
        i.user.add(u)
        print('write ')

        return JsonResponse({'date':date,'time_bucket': INTERVIEW_TIME_BUKET[i.tb_id],'tb_id':tb_id,'remaining':int(num-count-1)})

class MyRerservation(View):
    def get(self,request,user_id):
        dataList = []

        # 查询实验预约表
        query = ReservationInfo.objects.filter(user_id=user_id)

        u = UserInfo.objects.get(id=user_id)
        # 通过用户表查询关联的interviewinfo（面试预约表），返回查询集
        intv_query = u.interviewinfo_set.filter()
        # 通过用户表查询关联的中间表，返回中间表的数据
        inter_user_obj = u.interviewinfo_set.through.objects.filter(userinfo_id=u.id)
        intvList = []
        for q in intv_query:
            # 查询该时段共有多少个人预约
            i = InterviewInfo.objects.filter(date=q.date, tb_id=q.tb_id)[0]
            data = {
                'date':datetime.datetime.strftime(q.date, '%Y-%m-%d'),
                'tb_id':q.tb_id,
                'time_bucket': INTERVIEW_TIME_BUKET[q.tb_id],
                'count':i.user.count()
            }
            intvList.append(data)
        print(intvList)


        # 将查询结果按日期分组统计，这一步需要将日期格式挂成天数在分组，因此需要extra
        # <QuerySet [('2019-09-04', 2), ('2019-09-06', 1), ('2019-09-07', 2), ('2019-09-08', 2), ('2019-09-09', 2)]>
        date_tuple = query.extra(select={'date':"DATE_FORMAT(date,'%%Y-%%m-%%d')"})\
            .values('date').annotate(count=Count('date'))\
            .values_list('date','count')

        if not query:
            return JsonResponse({'msg':'还没有预约'})

        # 将queryset转换成生成器，可以连续迭代下去
        gene = (x for x in query)
        # 获取当前时间，判断是否临进实验，如果是，
        today = datetime.datetime.today()
        now = datetime.datetime.now()

        for date,count in date_tuple:
            tbs = []
            for i in range(count):
                q = next(gene)
                tbs_dict = {'tb_id': q.tb_id, 'time_bucket': TIME_BUKET[q.tb_id]}
                if q.date == today and q.tb_id == time_to_lab(now.hour,now.min):
                    tbs_dict['time_to_lab'] = True

                tbs.append(tbs_dict)
            data = {
                'date': date,
                'userid': user_id,
                'tbs':tbs,

            }
            dataList.append(data)
        # print(dataList)
        return JsonResponse([dataList,intvList],safe=False)

    def post(self,request):
        json_str = request.body.decode()
        req_data = json.loads(json_str)
        date = req_data.get('date')
        user_id = req_data.get('userid')
        tb_id = req_data.get('tb_id')
        print(date,user_id,tb_id)
        q = ReservationInfo.objects.filter(date=date,user_id=user_id,tb_id=tb_id)[0]
        q.user_id = None
        q.save()

        response = self.get(request,user_id)

        return response
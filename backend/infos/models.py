from django.db import models
from users.models import UserInfo

# Create your models here.
class ReservationInfo(models.Model):
    date = models.DateField(verbose_name='预约日期')
    tb_id = models.SmallIntegerField(verbose_name='预约时段')
    user = models.ForeignKey(UserInfo,on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = 'tb_reservationinfo'
        verbose_name = '实验预约信息表'
        verbose_name_plural = verbose_name

class InterviewInfo(models.Model):
    date = models.DateField(verbose_name='预约日期')
    tb_id = models.SmallIntegerField(verbose_name='预约时段')
    num = models.SmallIntegerField(default=10)
    user = models.ForeignKey(UserInfo,on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = 'interview'
        verbose_name = '面试预约信息表'
        verbose_name_plural = verbose_name
from django.db import models
from users.models import UserInfo

# Create your models here.
class ReservationInfo(models.Model):
    date = models.DateField(verbose_name='预约日期')
    tb_id = models.SmallIntegerField(verbose_name='预约时段')
    user = models.ForeignKey(UserInfo,on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = 'tb_reservationinfo'
        verbose_name = '预约信息表'
        verbose_name_plural = verbose_name
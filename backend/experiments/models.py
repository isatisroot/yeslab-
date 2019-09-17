from django.db import models

# Create your models here.
class LabAdress(models.Model):
    """
    创建记录rock和lab的ip的自关联表
    """
    name = models.CharField(max_length=20,verbose_name='Rock或Lab名')
    adress = models.CharField(max_length=60,verbose_name='实验接口')
    rockName = models.ForeignKey('self',null=True,blank=True,verbose_name='从属哪个Rock',on_delete=models.SET_NULL)

    class Meta:
        db_table = 'tb_labadress'
        verbose_name = '实验地址表'
        verbose_name_plural = verbose_name
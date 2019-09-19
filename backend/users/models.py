from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=12,unique=True,verbose_name='用户名')
    password = models.CharField(max_length=12,verbose_name='密码')
    realname = models.CharField(max_length=20, verbose_name='真实姓名',default='')
    email = models.CharField(max_length=50,verbose_name='邮箱',default='')
    phone = models.CharField(max_length=11,verbose_name='手机号',default='')
    qq = models.CharField(max_length=11,verbose_name='QQ',default='')
    adress = models.CharField(max_length=30,verbose_name='学校/企业名称',default='')
    # objects = models.Manager()
    class Meta:
        db_table = 'tb_userinfo'
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.realname
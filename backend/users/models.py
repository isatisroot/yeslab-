from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=11,unique=True,verbose_name='用户名')
    password = models.CharField(max_length=12,verbose_name='密码')
    email = models.CharField(max_length=50,verbose_name='邮箱')

    class Meta:
        db_table = 'tb_userinfo'
        verbose_name = '用户信息表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
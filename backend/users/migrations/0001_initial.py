# Generated by Django 2.2.3 on 2019-08-30 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=11, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=12, verbose_name='密码')),
                ('email', models.CharField(max_length=50, verbose_name='邮箱')),
            ],
            options={
                'verbose_name_plural': '用户信息表',
                'verbose_name': '用户信息表',
                'db_table': 'tb_userinfo',
            },
        ),
    ]

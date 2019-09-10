# Generated by Django 2.2.5 on 2019-09-10 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0005_auto_20190910_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interviewinfo',
            name='date',
            field=models.DateField(verbose_name='开放预约日期'),
        ),
        migrations.AlterField(
            model_name='interviewinfo',
            name='tb_id',
            field=models.SmallIntegerField(choices=[(1, '上午'), (2, '下午')], verbose_name='开放面试时段'),
        ),
        migrations.AlterField(
            model_name='interviewinfo',
            name='user',
            field=models.ManyToManyField(null=True, to='users.UserInfo'),
        ),
    ]

# Generated by Django 2.2.3 on 2019-09-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infos', '0011_reservationinfo_lab_adress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservationinfo',
            name='tb_id',
            field=models.SmallIntegerField(choices=[(1, '00:00-6:00'), (2, '6:30-10:30'), (3, '11:00-15:00'), (4, '15:30-19:30'), (5, '20:00-24:00')], verbose_name='预约时段'),
        ),
    ]
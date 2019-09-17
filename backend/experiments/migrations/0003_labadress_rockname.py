# Generated by Django 2.2.3 on 2019-09-17 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('experiments', '0002_remove_labadress_rockname'),
    ]

    operations = [
        migrations.AddField(
            model_name='labadress',
            name='rockName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='experiments.LabAdress', verbose_name='从属哪个Rock'),
        ),
    ]

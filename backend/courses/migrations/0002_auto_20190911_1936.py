# Generated by Django 2.2.3 on 2019-09-11 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseschedule',
            name='coursedate',
        ),
        migrations.RemoveField(
            model_name='courseschedule',
            name='teacher',
        ),
        migrations.DeleteModel(
            name='CourseDate',
        ),
        migrations.DeleteModel(
            name='CourseSchedule',
        ),
        migrations.DeleteModel(
            name='TeacherInfo',
        ),
    ]
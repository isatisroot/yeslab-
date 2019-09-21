from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from django.views.generic import View
from courses.models import CourseSchedule,CourseDate,TeacherInfo
import datetime,json


class Course(View):
    def get(self, request):
        course_month = CourseDate.objects.raw(
            'select * from tb_coursedate where '
            '(PERIOD_DIFF( date_format( date, "%%Y%%m" ), date_format( now( ) , "%%Y%%m" ) ) =-1 '
            'OR PERIOD_DIFF( date_format( date, "%%Y%%m" ), date_format( now( ) , "%%Y%%m" ) ) =0 '
            'OR PERIOD_DIFF( date_format( date, "%%Y%%m" ), date_format( now( ) , "%%Y%%m" ) ) =1)'
            'AND opendate <> 1;'
        )
        course_list = []
        for month in course_month:
            courses = month.courseschedule_set.all()
            for course in courses:
                data = {
                    'name': CourseSchedule.COURSE_CHOICE[course.course-1][1],
                    'date': course.coursedate.date,
                    'type': CourseSchedule.COURSETYPE_CHOICE[course.coursetype-1][1],
                    'time': course.schooltime,
                    'teacher': course.teacher.teacher
                }
                course_list.append(data)
        return JsonResponse(course_list, safe=False)

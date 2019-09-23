from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'course/1/$', views.Course.as_view()),
    url(r'course/2/$', views.Activity.as_view()),
]

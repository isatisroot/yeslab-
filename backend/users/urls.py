from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'captcha/(?P<uuid>.*)/$',views.Regiter.as_view()),
    url(r'register/$', views.Regiter.as_view()),

]
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'get_info/$',views.Reservation.as_view()),

    ]
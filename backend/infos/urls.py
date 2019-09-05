from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'get_info/$',views.Reservation.as_view()),
    url(r'sub_rv/$',views.Reservation.as_view()),
    url(r'get_reservation/(?P<user_id>\d+)/$',views.MyRerservation.as_view()),
    url(r'cancel_rv/$',views.MyRerservation.as_view())

    ]
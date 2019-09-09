from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'experiment/$',views.Experiment.as_view()),
    ]
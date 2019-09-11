import xadmin
from xadmin import views

from . import models

class InterviewAdmin(object):
    model_icon = 'fa fa-table'
class ReservationAdmin(object):
    model_icon = 'fa fa-flask'
xadmin.site.register(models.InterviewInfo,InterviewAdmin)
xadmin.site.register(models.ReservationInfo,ReservationAdmin)

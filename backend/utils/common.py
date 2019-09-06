import datetime
from .constant import TIME_TO_LAB,TIME_BUKET


def time_to_lab(hour,min):
    if min >= 30:
        score = hour*2 + 2
    else:
        score = hour *2 + 1

    for k in TIME_TO_LAB.keys():
        for item in k:
            if score ==item:
                v = TIME_TO_LAB[k]

                return v





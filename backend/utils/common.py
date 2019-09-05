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


def make_format_resp(query):
    dataList = []
    for q in query:
        data = {
            'date': datetime.datetime.strftime(q.date, '%Y-%m-%d'),

            'userid': q.user_id,
            'tb_id': q.tb_id,
            'time_bucket': TIME_BUKET[q.tb_id]
        }
        dataList.append(data)

    return dataList

from datetime import datetime
import time

jieduan = ((10, 0), (10, 30), (11, 0), (11, 30), (13, 30), (14, 0), (14, 30), (15, 0), (11, 2), (13, 2), (11, 9))



def get_time(d):
    if d.isoweekday() not in (6, 7):
        for n, i in enumerate(jieduan):
            if d.hour == i[0] and d.minute == i[1]:
                print(f"现在时间{d.hour}时{d.minute}分,{n+1}")
                return 1

    return 0


while 1:
    d = datetime.today()  # 获取当前日期时间
    val = get_time(d)
    print(val)
    time.sleep(13)

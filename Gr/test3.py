import  datetime


cc = datetime.datetime.now()
dd = datetime.timedelta(days=-1)
# print(cc, cc.hour)
# print(dd+cc)
# 根据当前小时取日期，15-20点为当天时间，其他取昨天
if 15 <= cc.hour <= 20:   # 时间在 15：00到20：00间
    riqi_2 = cc.strftime("%Y-%m-%d")
else:
    riqi_2 = (cc+dd).strftime("%Y-%m-%d")

print(riqi_2)

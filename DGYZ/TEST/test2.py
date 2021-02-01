import calendar
import datetime
from datetime import timedelta

now = datetime.datetime.now()
# 获取上月第一天和最后一天
last_month_end = datetime.date(now.year, now.month, 1) - timedelta(1)
last_month_start = datetime.date(last_month_end.year, last_month_end.month, 1)
print(last_month_start, last_month_end)

# 获取本月第一天和最后一天：
this_month_start = datetime.datetime(now.year, now.month, 1)
this_month_end = datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1])

test_dict = {1: last_month_start, 2: last_month_end}
print(test_dict[1])
print(test_dict[2])

#######################################################
# 获取今天日期：
now = datetime.datetime.now()  # 返回datetime格式：eg：2019-12-07 20:38:35.82816
# print(now)
now = datetime.datetime.now().date()  # 返回datetime格式：eg：2019-12-07
# print(now)
now = datetime.date.today()
# print(now)

# 获取昨天日期：
yesterday = now - timedelta(days=1)

# 获取明天日期：
tomorrow = now + timedelta(days=1)

# 获取本周第一天和最后一天：
this_week_start = now - timedelta(days=now.weekday())
this_week_end = now + timedelta(days=6 - now.weekday())
# print(this_week_start, this_week_end)

# 获取上周第一天和最后一天：
last_week_start = now - timedelta(days=now.weekday() + 7)
last_week_end = now - timedelta(days=now.weekday() + 1)

# 获取本月第一天和最后一天：
this_month_start = datetime.datetime(now.year, now.month, 1)
this_month_end = datetime.datetime(now.year, now.month, calendar.monthrange(now.year, now.month)[1])

"""注：
calendar.monthrange(year,month)
传入两个值：一个是当前的年份，另外一个是当前的月份
写法可以是：calendar.monthrange(now.year,now.month)

返回两个整数。
第一个值为该月第一天所在的星期几，对应的数字。0 - 6==>0（星期一）到6（星期日）
第二个值为该月一共几天。"""

# 获取上月第一天和最后一天 ：
last_month_end = this_month_start - timedelta(days=1)
last_month_start = datetime.datetime(last_month_end.year, last_month_end.month, 1)

# 获取本季第一天和最后一天：
month = (now.month - 1) - (now.month - 1) % 3 + 1
this_quarter_start = datetime.datetime(now.year, month, 1)
this_quarter_end = datetime.datetime(now.year, month, calendar.monthrange(now.year, now.month)[1])

# 获取上季第一天和最后一天：
last_quarter_end = this_quarter_start - timedelta(days=1)
last_quarter_start = datetime.datetime(last_quarter_end.year, last_quarter_end.month - 2, 1)

# 获取本年第一天和最后一天：
this_year_start = datetime.datetime(now.year, 1, 1)
this_year_end = datetime.datetime(now.year + 1, 1, 1) - timedelta(days=1)

# 获取去年第一天和最后一天：
last_year_end = this_year_start - timedelta(days=1)
last_year_start = datetime.datetime(last_year_end.year, 1, 1)

"""最后，如果要获取到date的格式，在最后加上".date"就能实现啦。"""

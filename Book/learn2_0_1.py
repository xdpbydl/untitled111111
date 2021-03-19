import datetime

# 如果时间不为整点，有分钟，有秒，有毫秒呢？ 7:6 -- 8:6
pepole_time_l = {'a': ('6:01', '6:12'),
                 'b': ('7:00', '8:12'),
                 'c': ('10:00', '10:55'),
                 'd': ('10:00', '12:02'),
                 'e': ('8:05', '10:5'),
                 'f': ('9:00', '9:30'),
                 'g': ('13:00', '13:10'),
                 'h': ('14:00', '14:05'),
                 'i': ('14:33', '14:55'),
                 'j': ('7:00', '14:30'),
                 }


def parse_time(s):
    """
    字符串转为时间
    :param s:
    :return:
    """
    hh_s, mm_s = s.split(':')
    return datetime.time(hour=int(hh_s), minute=int(mm_s))


def no_time(s, d='t'):
    if d == 't':
        hh_s, mm_s = s.split(':')
        return int(hh_s) * 60 + int(mm_s)
    elif d == 'd':
        hh_s, mm_s = divmod(s, 60)
        return f'{hh_s}:{mm_s}'


def get_val(dict_tol, c_n=60):
    """

    :param dict_tol: 目标字典
    :param c_n: 拜访者可以呆的时间
    :return:
    """
    new_dict = {}
    count_list = []
    m = n = 0
    for key, val in dict_tol.items():
        val_a = no_time(val[0])
        val_b = no_time(val[1])
        new_dict[key] = [val_a, val_b]
    list_min = sorted(new_dict.items(), key=lambda new_dict: new_dict[1][0], reverse=False)
    list_max = sorted(new_dict.items(), key=lambda new_dict: new_dict[1][1], reverse=True)

    min_time = list_min[0][1][0]
    max_time = list_max[0][1][1]
    # print(min_time, max_time)

    for i in range(min_time, max_time):
        m = 0
        end = i + c_n
        p_str = ''
        for t in list_min:
            if t[1][0] <= i < t[1][1] or t[1][0] < end < t[1][1]:
                m += 1
                p_str += t[0] + ','
        if n <= m:
            n = m
            count_list.append([n, i, end, p_str])
    lv_n = count_list[-1][0]
    lv_list = []
    # print(count_list)
    for i in count_list:
        if i[0] == lv_n:
            lv_list.append(i[1:])

    # print(lv_list, '--'*18)
    start_a = no_time(lv_list[0][0], 'd')
    start_b = no_time(lv_list[-1][0], 'd')
    end_a = no_time(lv_list[0][1], 'd')
    end_b = no_time(lv_list[-1][1], 'd')
    p_str_sum = lv_list[-1][2]
    return f"最佳时间段为：{start_a}或{start_b}开始,到{end_a}或{end_b}结束。可以约见{lv_n}人，分别为{p_str_sum}。"


print(get_val(pepole_time_l, 60))
print(get_val(pepole_time_l, 30))
print(get_val(pepole_time_l, 5))

pepole_time_l = {'a': (6, 7), 'b': (7, 9), 'c': (10, 11), 'd': (10, 12), 'e': (8, 10), 'f': (9, 11), 'g': (6, 8)}

count_dict = {}
m = n = 0


def greeting(key, pepole):
    if count_dict.get(key, '不存在') == '不存在':
        count_dict[key] = [1, pepole]
    else:
        count_dict[key][0] += 1
        count_dict[key][1] += ',' + pepole


def get_max_count(dict_time):
    for i, val in dict_time.items():
        for c in range(val[0], val[1]):
            greeting(c, i)

    # 按照  count_dict[1][0] 值进行降序排列
    ict2 = sorted(count_dict.items(), key=lambda count_dict: count_dict[1][0], reverse=True)
    print(f'最佳时间为{ict2[0][0]}到{ict2[0][0] + 1}点, 可以约见{ict2[0][1][0]}个人，分别为{ict2[0][1][1]}。')


get_max_count(pepole_time_l)

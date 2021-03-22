def get_e_str(in_num=500, A_a='A', if_str=False):
    """
    查询excel列的信息
    :param in_num: 为多少列
    :param A_a:    默认列名：'A'为大写，'a'为小写
    :param if_str:  默认列名False，存在侧查询是第多少列
    :return:  多少列
    """
    if A_a == 'a':
        set_num = 97
    elif A_a == 'A':
        set_num = 65
    in_num_0 = in_num // 26
    for i_1 in range(in_num_0 + 1):
        if i_1 == 0:
            set_str = ''
        else:
            set_str = '%c' % (set_num + i_1 - 1)
        for i in range(26):
            num = set_num + i
            if "%s%c" % (set_str, num) == if_str:
                print(i_1 * 26 + i + 1)
                return i_1 * 26 + i + 1
            elif in_num_0 == i_1 and i == in_num % 26:
                break
            if not if_str:
                print("%s%c, " % (set_str, num), end='')


get_e_str(in_num=10)  # 查询1到10列的列名
get_e_str(in_num=27, A_a='a')  # 查询1到27列的列名，以小写方式

get_e_str(if_str='BB')  # 查询AS列,是第几列

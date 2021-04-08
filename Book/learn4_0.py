# 第四节，皇后分离

def set_list_val(ch_list, y, x, num):
    for x2 in range(num):
        if ch_list[y][x2] == 0:
            ch_list[y][x2] = 3
            # print('222' * 8, ch_list[y][x2])
        if ch_list[x2][x] == 0:
            ch_list[x2][x] = 3
        if y + x2 < num and x + x2 < num:
            if ch_list[y + x2][x + x2] == 0:
                ch_list[y + x2][x + x2] = 3
        if y - x2 >= 0 and x - x2 >= 0:
            if ch_list[y - x2][x - x2] == 0:
                ch_list[y - x2][x - x2] = 3
        if y - x2 >= 0 and x + x2 < num:
            if ch_list[y - x2][x + x2] == 0:
                ch_list[y - x2][x + x2] = 3
        if x - x2 >= 0 and y + x2 < num:
            if ch_list[y + x2][x - x2] == 0:
                ch_list[y + x2][x - x2] = 3


def set_list_True(ch_list, y, x, num):
    for x2 in range(num):
        if ch_list[y][x2] == 1:
            return True
        if ch_list[x2][x] == 1:
            return True
        if y + x2 < num and x + x2 < num:
            if ch_list[y + x2][x + x2] == 1:
                return True
        if y - x2 >= 0 and x - x2 >= 0:
            if ch_list[y - x2][x - x2] == 1:
                return True
        if y - x2 >= 0 and x + x2 < num:
            if ch_list[y - x2][x + x2] == 1:
                return True
        if x - x2 >= 0 and y + x2 < num:
            if ch_list[y + x2][x - x2] == 1:
                return True

    ch_list[y][x] = 1
    # print(ch_list[y][x]), input('@'*12)
    return False


def get_rule(ch_list):
    num = len(ch_list)
    for x in range(num):
        for y in range(num):
            if ch_list[y][x] == 1:
                set_list_val(ch_list, y, x, num)
            elif ch_list[y][x] == 0:
                if not set_list_True(ch_list, y, x, num):
                    set_list_val(ch_list, y, x, num)
    return ch_list


def chess_queen(m=8):
    chess_l = [[0 for _ in range(m)] for _ in range(m)]
    chess_l[0][0] = 1
    for i in range(m):
        for i2 in range(m):
            chess_l = get_rule(chess_l)
    for i in range(m):
        print(chess_l[i])


chess_queen()

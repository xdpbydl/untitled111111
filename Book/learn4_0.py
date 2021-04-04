# 第四节，皇后分离

def chess_queen(m=8):
    chess_l = [[0 for _ in range(m)] for _ in range(m)]


    def set_temp(chess_l):
        ch_no = 0
        for lei, i in enumerate(chess_l):  # 列
            for han, i_2 in enumerate(i):  # 行
                if i_2 == 0:
                    for x in range(m):
                        if chess_l[x][i_2] == 0:
                            chess_l[x][i_2] = 'a'
                        if chess_l[han][x] == 0:
                            chess_l[han][x] = 'a'
                        # if chess_l
                    chess_l[lei][han] = 1
                    ch_no += 1
                    # print(chess_l), input()
                else:
                    continue
        print(chess_l, ch_no)

    set_temp(chess_l)


chess_queen()


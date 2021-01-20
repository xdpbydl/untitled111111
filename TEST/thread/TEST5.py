dg_d = {1: {'index': 1, 'name': 'A表', '条件': {1: '支行', 2: '日期1', 3: '业务1'}},
        2: {'index': 1, 'name': 'B表', '条件': {1: '支行', 2: '日期2', 3: ["啊","C","D"]}},
        3: {'index': 1, 'name': 'C表', '条件': {1: '支行', 2: '日期3', 3: '业务3'}}}




for key, value in dg_d.items():
        # print(key, value)
        for key1, value1 in value.items():
                # print(key1, value1)
                # if key1=='条件':
                #         print(f'{key}, {key1}, {value1}')
                # if key1 == '条件':
                #         for key2, value2 in value1.items():
                #                 print(key2, value2)
                pass
print(dg_d[2]['条件'][3][2])
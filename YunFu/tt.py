import pandas as pd


excel_file = r'E:\TEMP\6TEST\yz_temp\高一级学生信息.xlsx'
excel_file_t = r'D:\TEST1.xlsx'
df = pd.read_excel(excel_file, header=None)

new_loc = ['封箱完工录入', '', '', '', '', '', '', '', '', '', '', '', '']
test_dict = {12: [1, 1, 2], 13: [2, 3, 4], 15: 'dffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'}
# test_dict = {12: 'dd', 13: 22}
df.columns = new_loc
test_dict[13].remove(3)
txt_file = r"D:\\test.txt"
# print(df)

with open(txt_file, "w") as f:
    f.write(str(test_dict))



with open(txt_file, "r") as f:
    data = f.readline()
    print(data)
    data = eval(data)



# data = pd.DataFrame({'ct': [1, 1, 2, 2, 3], '1_tf': [10, 20, 30, 40, 50]})
# # co_1f_dict = data.groupby('ct')['1_tf'].sum().to_dict()
# co_1f_dict = data.groupby('ct')['1_tf'].mean().to_dict()
#
# a = data['ct'].reset_index(drop=True)
# # print(a)
#
# print(a.iloc[0])
#
# print(co_1f_dict[a.iloc[0]])
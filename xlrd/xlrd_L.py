import xlrd

# 打开Excel文件读取数据
file = r'E:\LTT\4. 狮之谦资料\8.26面料情况.xls'
data = xlrd.open_workbook(file)

sheet_name = data.sheet_names()  # 获取所有sheet名称
# print(sheet_name)  # ['银行2', '银行3']

# 根据下标获取sheet名称
sheet2_name = data.sheet_names()[-1]
# print(sheet2_name)  # '银行3'

# 根据sheet索引或者名称获取sheet内容，同时获取sheet名称、列数、行数
sheet2 = data.sheet_by_index(1)
# print('sheet2名称:{}\nsheet2列数: {}\nsheet2行数: {}'.format(sheet2.name, sheet2.ncols, sheet2.nrows))
# print(sheet2.row_values(0))
# print(sheet2.row_values(1))

sheet1 = data.sheet_by_name('8.26预热数据')
# print('sheet1名称:{}\nsheet1列数: {}\nsheet1行数: {}'.format(sheet1.name, sheet1.ncols, sheet1.nrows))

# print(sheet1.col_values(0)[12])


# # 获取指定单元格的内容
# print(sheet1.cell(1, 0).value)  # 第2 行1列内容
# print(sheet1.cell_value(1, 0))  # 第2 行1列内容
# print(sheet1.row(1)[0].value)  # 第2 行1列内容
#
#
# # 获取单元格内容的数据类型
# print(sheet1.cell(1,0).ctype)  # 第2 行1列内容 ：机构名称为string类型
# print(sheet1.cell(3,4).ctype)  # 第4行5列内容：999 为number类型
# print(sheet1.cell(3,6).ctype)  # 第4 行7列内容：2013/7/8 为date类型
# # 说明：ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error

#
# from datetime import datetime, date
#
# if sheet1.cell(1, 2).ctype == 3:
#     print(sheet1.cell(1, 2).value)  # 41463.0
#     date_value = xlrd.xldate_as_tuple(sheet1.cell(1, 2).value, data.datemode)
#     print(date_value)  # (2013, 7, 8, 0, 0, 0)
#     print(date(*date_value[:3]))  # 2013-07-08
#     print(date(*date_value[:3]).strftime('%Y/%m/%d'))  # 2013/07/08

# print(sheet1.cell(4, 1))
# if sheet1.cell(4, 1).ctype == 2:
#     print(sheet1.cell(4, 1).value)  # 133111.0
#     num_value = int(sheet1.cell(4, 1).value)
#     print(num_value)  # 133111


# 这里，需要在读取文件的时候添加个参数，将formatting_info参数设置为True，默认是False，否
# 则可能调用merged_cells属性获取到的是空值。<br>
data = xlrd.open_workbook(file, formatting_info=True)
sheet1 = data.sheet_by_index(-1)
print(sheet1.merged_cells)  # [(0, 1, 0, 8), (2, 6, 0, 1)]<br>
# merged_cells返回的这四个参数的含义是：(row,row_range,col,col_range),其中[row,row_range)包括row,
# 不包括row_range,col也是一样，下标从0开始。
# (0, 1, 0, 8) 表示1列-8列合并 (2, 6, 0, 1)表示3行-6行合并<br>
# 分别获取合并2个单元格的内容：
print(sheet1.cell(0, 0).value)  # 银行2
print(sheet1.cell_value(3, 0))  # 银行2

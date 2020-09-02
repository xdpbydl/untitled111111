import openpyxl
import pandas as pd

excel_file = r'E:\TEMP\02GR\kefahuo\HANG\可发货通知书(代运）2020——导入2.0_1.xlsx'  # 格式文件
save_file = r'E:\TEMP\02GR\kefahuo\geshi\new_save.xlsx'  # 保存的新文件
data_fiel = r'E:\TEMP\02GR\kefahuo\可发货通知单报表.xls'  # 数据文件

wb_yuan = openpyxl.load_workbook(excel_file)
wb_data = openpyxl.load_workbook(data_fiel)
# print(wb_yuan.sheetnames)
sheet = wb_yuan["Sheet1"]
# print (sheet['d4'].value)



# for i in sheet[2]:
    # print(i.value, end=" ")


# xl = openpyxl.Workbook()
# xls = xl.create_sheet(index=0)  # 新建一个excel，sheet表
# """通讯录"""
# list1 = ["年龄", "姓名", "手机号码"]  # 这里是我们需要的字段，可以根据需要自行添加，删除，修改
# for i in range(1, 40000):  # 这里是我们需要的行数。比如这里是4万
#     for j, value in enumerate(list1):
#         if j == 0:
#             xls.cell(i, 1).value = str(i)  # 根据特殊字段进行处理，输入不同的数值。可以自行添加其他需要的字段。
#         else:  # 其他情况或者没有特殊字段，直接使用添加列表中的值代替。
#             xls.cell(i, j + 1).value = value
#
# xl.save(save_file)  # 保存我们生成的数据

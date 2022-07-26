import openpyxl


# model_file = "E:\\JiaZhi\\0.3 HUA\\AB.xlsx"
file_ab = "E:\\JiaZhi\\0.3 HUA\\AB.xlsx"
wb = openpyxl.load_workbook(file_ab, data_only=True)

# new = wb.copy_worksheet(wb.worksheets[1])
# new.title = "-1"
# wb.save(file_ab)

#
# n_str = "121,2882,1212"
# n_list = n_str.split(',')
# print(n_list, type(n_list))
# try:
#     n_list.remove(2882)
# except:
#     pass
# print(n_list)

po_no = 901283112
with open(r'E:\TEMP\6TEST\0DEL\明细保存进度.txt',"r") as f:  # 打开文件
    po_data = f.read()  # 读取文件
    print(po_data)
with open(r'E:\TEMP\6TEST\0DEL\明细保存进度.txt', "w+") as f:  # 打开文件
    po_data_list = po_data.strip(' ').split(',')
    print(po_data_list)
    try:
        po_data_list.remove(str(po_no))
    except:
        print(f'{po_no}移除失败')
    po_data_rust = ','.join(map(str, po_data_list))
    f.write(po_data_rust)


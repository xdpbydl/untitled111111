import openpyxl

# model_file = "E:\\JiaZhi\\0.3 HUA\\AB.xlsx"
file_ab = "E:\\JiaZhi\\0.3 HUA\\AB.xlsx"
wb = openpyxl.load_workbook(file_ab,  data_only=True)

new = wb.copy_worksheet(wb.worksheets[1])
new.title = "-1"
wb.save(file_ab)
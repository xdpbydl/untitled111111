import os, pandas as pd, time, datetime

aa = 1
export_file = r"C:\Users\Administrator\Desktop\11.xlsx"
excel_data = pd.read_excel(export_file, index=False)

if len(excel_data) == 0:
    aa = 0


# print(aa)
dtime = datetime.datetime.today()
# print(dtime)
# datetime.datetime.strftime('%Y-%m-%d', dtime )
bb = dtime.strftime("%Y-%m-%d")
print(bb)
# b = datetime.datetime.strptime(dtime, '%Y-%m-%d').strftime('%m-%d')

import pandas as pd


excel_file = r'E:\TEMP\6TEST\GF0100.xls'
excel_save = excel_file.replace('GF0100.xls', 'GF0100__1.xls')
df = pd.read_excel(excel_file)
print(df)

df.to_excel(excel_save, index=False)

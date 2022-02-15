import pandas as pd

canshu_file = r'E:\TEMP\6TEST\GRWL\duichongkuai\model\参数.xlsx'

canshu_df = pd.read_excel(canshu_file)

q_day = canshu_df.loc[canshu_df['参数名称'] == '向前取天数', ['参数值']].values
h_day = canshu_df.loc[canshu_df['参数名称'] == '向后取天数', ['参数值']].values

if h_day < 100 and q_day > -100:
    aa = int(h_day)

print(aa, type(aa))
a = canshu_df.loc[[1], ['参数名称']]
print(a)
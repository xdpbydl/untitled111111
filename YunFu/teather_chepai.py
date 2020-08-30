import pandas as pd


x_path = r'E:\TEMP\01YZ\车牌对应' + '\\'
t_exle = 'all_.xls'
chepai_exle = '2020年7月云浮中学教职工小车车牌登记表+++.xls'
save_file = 'save_all.xls'
daoru_file = r'E:\TEMP\01YZ\车牌对应\导入老师_20200816.xls'


te = pd.read_excel(x_path + t_exle, index=False)
chepai = pd.read_excel(x_path + chepai_exle, index=False)
chepai.drop(['序号'], axis=1, inplace=True)
# print(te)
# print(chepai)

#  车牌'姓名', '小车车牌号码1'去重
# print(chepai)
chepai_1 = chepai.drop_duplicates(subset=['姓名', '小车车牌号码1'], keep='first')
# print(chepai_1)


df = pd.merge(te, chepai_1, on=['姓名','姓名'], how='left')
# print(df)
df.to_excel(x_path + save_file, index=False)

# #  获取重复索引，然后取交集，然后筛选出来。该方法保留了原来的索引，缺点是数据原索引不能有重复
# t = chepai
# index1 = t[t[['姓名']].duplicated(keep="last")].index
# index2 = t[t[['姓名']].duplicated(keep="first")].index
# t1 = t.loc[index1 | index2, :]
# print(t1)
daoru_df = pd.read_excel(daoru_file, index=False)


print(len(daoru_df.车牌号码))
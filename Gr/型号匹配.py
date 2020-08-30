import pandas as pd
import numpy as np

arry = pd.read_excel(r'基础信息.xlsx')
df = pd.read_excel(r'可发货通知书.xlsx')

# print(arry)
arry.sort_values("型号", inplace=True)
# print(arry)

df["金额"] = 0
df["型号"] = df["型号"].astype("string")
arry["型号"] = arry["型号"].astype("string")

# df = df.query('MAX in 型号')
# print(arry)
# arry 0索引,1金额,2层标准, 0 曾 1高
types = []
count = len(arry)
for i in range(len(df)):
    for ix in range(len(arry)):
        if df["型号"][i].upper().find(arry["型号"][ix].upper()) > -1:
            if arry["层数"][ix] > 0:
                types = [ix, arry["价格"][ix], arry["层数"][ix], 0]
            elif arry["高度"][ix] > 0:
                types = [ix, arry["价格"][ix], arry["高度"][ix], 1]
            else:
                types = [ix, arry["价格"][ix], arry["层数"][ix], 0]
            # arry表全部遍历完后再来进行赋值，赋值最后一次所得到的types值

        if count == ix + 1:
            # 曾和高统一按照 层 取 如要区分列  拿types最后一位区分按曾或者高
            if df["层"][i] <= types[2]:  # 在标准价格方位内
                df.loc[i, "金额"] = types[1]
            else:
                df.loc[i, "金额"] = types[1] + (df["层"][i] - types[2]) * 10000
            types = []

df.to_excel(r'new可发货通知书.xlsx')

import pandas as pd

diqu_file = r'E:\ZCXX\广日物流\1. RPA\3. 实施\地区信息.xlsx'
df_file = r'E:\TEMP\02GR\kefahuo\可发货通知书(代运）2020——导入2.0______1.xlsx'
diqu_1 = pd.read_excel(diqu_file, sheet_name="省内区级")
diqu_2 = pd.read_excel(diqu_file, sheet_name="省内市级")
diqu_3 = pd.read_excel(diqu_file, sheet_name="省外")
df = pd.read_excel(df_file)

# diqu = diqu_1.append(diqu_2, diqu_3, ignore_index=False)
diqu = pd.concat([diqu_1, diqu_2, diqu_3])
diqu.sort_values("编号", inplace=True)
# aa = diqu.名称.tolist()
# bb = set(aa)
# print(len(aa),len(bb))

# df["安装地址"] = df["安装地址"].astype("string")
# diqu["名称"] = diqu["名称"].astype("string")
# df = df.applymap(str)
# diqu = diqu.applymap(str)


no_list = []
count = len(diqu)
for i in range(len(df)):
    for n in range(len(diqu)):

        if (diqu.iloc[n].名称) in df.iloc[i].安装地址:
            print(diqu.iloc[n].编号, diqu.iloc[n].名称, df.iloc[i].安装地址)
            no_list = [i, n, diqu.iloc[n].编号, diqu.iloc[n].名称]
            # print(no_list)


        if count == n + 1:
            print(no_list)
            if no_list == []:
                df.loc[i, "地区"] = ''
            else:
                df.loc[i, "地区"] = [no_list[-1]]
            no_list = []

            # print(df.iloc[no_list[0]].安装地址 , diqu.iloc[[no_list[1]], [1]])

    #
    # break
df.to_excel(df_file, index=False)

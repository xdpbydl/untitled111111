import pandas as pd

Excel_xiangtou_Path = r'C:\Users\Administrator\Desktop\grwl_log\20201020\箱头.xls'
save2 = Excel_xiangtou_Path.replace('.xls', '11_new.xls')
df2 = pd.read_excel(Excel_xiangtou_Path, header=1, keep_default_na=False)


def geshi(x):

    if x["层站门"] == '':
        aa = str(x["提升高度"]) + 'MM '
    elif x["层站门"].strip() == r'0/0/0':
        aa = r'0MM '
    else:
        aa = x["层站门"]
    return aa

df2["层站门"] = df2.apply(geshi, axis=1)

# df2["层站门"] = df2['提升高度'].apply(lambda x: x + 'MM ' if x == '' else '')
# df2["层站门"] = df2['提升高度'].apply(lambda x: x + '0MM ' if x == r'0\0\0' else '')

# df2['层站门'] = df2['层站门'].mask(df2['层站门'] == '', df2['提升高度'] + 'MM ')


# df2.loc[(df2['层站门']==''),['层站门']] =   'MM '
# print(df2)


df2.to_excel(save2, index=False)

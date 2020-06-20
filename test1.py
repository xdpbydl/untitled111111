import pandas as pd

WX = pd.read_excel('E:/TEMP/untitled111111/WX_File.xlsx')
print(len(WX))
# 对于每一行，通过列名name访问对应的元素
for idex, row in WX.iterrows():
    print(row['公众号'], row['最新文章'])
    if idex == 0:
        row['最新文章'] = 'aaa21212'
        WX.iloc[idex] = pd.Series(row)
    # print(row)
    # print(row['公众号'], row['最新文章'])




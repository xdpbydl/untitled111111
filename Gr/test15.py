import pandas as pd
from win32com.client import Dispatch

Excel_zhuangxiangInfo_Path = r'E:\TEMP\02GR\JobNuberInfo\11.xls'


# 另存为 因为Html网页格式表格不能读取，统一修改格式
def Save_Format_xls(filename):
    xlApp = Dispatch("Excel.Application")
    xlApp.Visible = False  # 后台运行
    xlApp.DisplayAlerts = False  # 不警报
    xlBook = xlApp.Workbooks.Open(filename)
    xlBook.SaveAs(filename, 51)  # 56   xls    51 xlsx
    xlBook.Close()


def Save_Formats_xls(filename, newfilename):
    xlApp = Dispatch("Excel.Application")
    xlApp.Visible = False  # 后台运行
    xlApp.DisplayAlerts = False  # 不警报
    xlBook = xlApp.Workbooks.Open(filename)
    xlBook.SaveAs(newfilename, 56)  # 56   xls    51 xlsx
    xlBook.Close()



Save_Format_xls(Excel_zhuangxiangInfo_Path)


# df1 = pd.read_html(Excel_zhuangxiangInfo_Path, keep_default_na=False)
df1 = pd.read_excel(Excel_zhuangxiangInfo_Path, keep_default_na=False)
# 删除不需要的列
# df1.drop(["装箱单编号", "版本", "使用单位", "井道图号", "提升高度"], axis=1, inplace=True)

# 根据excel中的宏设定，取"工号"、"零件编号"前11个字符，"图表号"前8个字符
# df1["工号"] = df1["工号"].str[:11]
# df1["零件编号"] = df1["零件编号"].str[:11]
# df1["图表号"] = df1["图表号"].str[:8]

# print(df1[["零件编号", "工号", "图表号"]])
# print(len(df1[0]))
print(len(df1))
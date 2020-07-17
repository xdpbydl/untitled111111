# import pdfplumber   #导入pdf包
# import re           #导入正则表达式包
#
# pdf_file = r'E:\ZCXX\广日物流\1. RPA\1. 需求调研\对重块\工牌\清单900911034.pdf'
# pdf = pdfplumber.open(pdf_file) #加载pdf
# page0 = pdf.pages[7]                      #取出第一页，你可以用for来遍历所有页面
# tables = page0.extract_tables()           #从page0里面取出多个tables
# texts = page0.extract_text()              #从page0里面取出所有文本
# # results = re.findall(r"([0-9]{1,3}(,[0-9]{3})*\.[0-9]+)", texts) #从文本中提取带千分位和小数点的数字
# print(texts)

import pdfplumber
import pandas as pd
pdf_file = r'E:\ZCXX\广日物流\1. RPA\1. 需求调研\对重块\工牌\清单900911034.pdf'
with pdfplumber.open(pdf_file) as pdf:
    # first_page = pdf.pages[7]
    # print(first_page.extract_words())


    # page = pdf.pages[8]   # 第一页的信息
    # text = page.extract_text()
    # print(text)
    # table = page.extract_tables()
    # # for t in table:
    # #     # 得到的table是嵌套list类型，转化成DataFrame更加方便查看和分析
    # #     df = pd.DataFrame(t[1:], columns=t[0])
    # #     print(df)

    p0 = pdf.pages[0]
    im = p0.to_image()
    aa = im.draw_rects(p0.extract_words())
    print(aa)

import pdfplumber   #导入pdf包
import re           #导入正则表达式包

pdf_file = r'E:\ZCXX\广日物流\1. RPA\1. 需求调研\对重块\工牌\清单900911034.pdf'
pdf = pdfplumber.open(pdf_file) #加载pdf
page0 = pdf.pages[7]                      #取出第一页，你可以用for来遍历所有页面
tables = page0.extract_tables()           #从page0里面取出多个tables
texts = page0.extract_text()              #从page0里面取出所有文本
# results = re.findall(r"([0-9]{1,3}(,[0-9]{3})*\.[0-9]+)", texts) #从文本中提取带千分位和小数点的数字
print(texts)

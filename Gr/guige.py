from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
import re
import pandas as pd
# 可以使用此方法获取网络上的pdf
from urllib.request import urlopen

pdf_file = r'E:\ZCXX\广日物流\1. RPA\1. 需求调研\对重块\工牌\清单900912571.pdf'
# fp = urlopen(pdf_file)

# 获取文档对象
fp = open(pdf_file, "rb")

# 创建一个一个与文档关联的解释器
parser = PDFParser(fp)

# PDF文档的对象
doc = PDFDocument()

# 连接解释器和文档对象
parser.set_document(doc)
doc.set_parser(parser)

# 初始化文档,当前文档没有密码，设为空字符串
doc.initialize("")

# 创建PDF资源管理器
resource = PDFResourceManager()

# 参数分析器
laparam = LAParams()

# 创建一个聚合器
device = PDFPageAggregator(resource, laparams=laparam)

# 创建PDF页面解释器
interpreter = PDFPageInterpreter(resource, device)

# 使用文档对象得到页面的集合
index, hang = 1, ''
GG = pd.DataFrame()
for page in doc.get_pages():
    data = ''
# if index == 1:
    print('--'*30 + str(index))
    # 使用页面解释器读取
    interpreter.process_page(page)

    # 使用聚合器来获得内容
    layout = device.get_result()

    hang = ''
    for out in layout:
        if hasattr(out, "get_text"):
            # print(type(out.get_text()))
            # print(out.get_text())
            hang += out.get_text()
    # if index == 1:
    #     print(hang)
    gonghao = re.findall(r'工号：.*', hang)[0].split(' ')[1]
    shuliang = re.findall(r'.*ea', hang)
    guige = re.findall(r'\n\b对重块\b\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n', hang)

    guige1 = re.findall(r'\d{1,}×\d{1,}×\d{1,}', str(guige))

    # print(shuliang, guige, guige1)
    if guige1 == []:    # 1\规格写在备注中,2\规格只有长宽
        guige1 = re.findall(r'\d{1,}×\d{1,}', str(guige))
        if guige1 == []:
            guige = re.findall(r'\n\bREMARK备注\b\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n', hang)
            guige1 = re.findall(r'\d{1,}×\d{1,}×\d{1,}', str(guige))
            if guige1 == []:
                guige1 = re.findall(r'\d{1,}×\d{1,}', str(guige))
                # print(shuliang, guige, guige1)
    # print(guige, len(guige))
    data = [guige1[i] + '=' + shuliang[i].split(' ')[0] for i in range(len(shuliang))]

    # for i in range(len(shuliang)):
    #     if i != len(shuliang)-1:
    #         data += guige1[i] + '=' + shuliang[i].split(' ')[0] + '\n'
    #     else:
    #         data += guige1[i] + '=' + shuliang[i].split(' ')[0]

    GG = GG.append({'工号': gonghao, '规格': '\n'.join(data)}, ignore_index=True)
    print(gonghao, '\n'.join(data))
    index += 1

GG.to_excel('12.xlsx', "Sheet1", index=False)


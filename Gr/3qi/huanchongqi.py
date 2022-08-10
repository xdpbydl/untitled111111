import os
import pdfplumber
import fitz
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter


pdf_file = r'E:\TEMP\6TEST\GRRPA\huanchongqi\testpdf.pdf'
pdf_file_c = r'E:\TEMP\6TEST\GRRPA\huanchongqi\testpdf_c.pdf'
save_file = r'E:\TEMP\6TEST\GRRPA\huanchongqi\testpdf_1.pdf'


# hg_list = ['18G086737','18G086737','18G086738','18G086738','18G086730','18G086730', '18G086731','18G086731','18G086735','18G086735','18G086736','18G086736','18G053959','18G053959','18G053960','18G053960','18G053958','18G053958','20G031154','20G031154']
hg_list = []
# output = PdfFileWriter()
# input1 = PdfFileReader(open(pdf_file, "rb"))
#
# #打印input1有多少页:*
# print ("document1.pdf has %d pages." % input1.getNumPages())


doc = fitz.open(pdf_file)

# page_n = doc.page_count
# page = doc.load_page(10) # 18G086735
# text = page.get_text()
# print(text)

# gh = doc[8].get_textbox("text")
# print(gh)
# input('--'*88)
# print(gh)

hg_list.sort()
print(hg_list)
hg_new = []
# for i in range(20):
for page in doc:
    # if i != 7:
    #     continue
    # page = doc[i]
    # page = doc.load_page(i)
    text = page.get_text()
    # if i in [0, 1]:
    #     print(text)
    text = text.split('\n')[8]
    # if i in [0,1]:
    #     print(text)
    # no = hg_list.index(text)
    i = page.number
    # print(text, i, no)
    hg_list.append(text)
    # weizhi = page.search_for("产品型号")
    # print(text)
    # print(page, i, weizhi)

# print(hg_list)

# for i, val in enumerate(hg_list):

hg_dict = dict(zip([x for x in range(len(hg_list))], hg_list))
hg_dict_O = sorted(hg_dict.items(),key=lambda x:x[1],reverse=False)

# print(hg_dict)
# print(hg_dict_O)
hg_list_n = [k for k,v in hg_dict_O]
print(hg_list_n)

doc.select(hg_list_n)
doc.save(save_file)
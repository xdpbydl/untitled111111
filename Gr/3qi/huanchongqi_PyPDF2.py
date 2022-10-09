from PyPDF2 import PdfFileMerger,PdfFileReader, PdfFileWriter
import os


Save_Path = 'E:\\TEMP\\6TEST\\GRRPA\\huanchongqi\\'
fns = [os.path.join(root, fn) for root, dirs, files in os.walk(Save_Path) for fn in files if ('ererer' ) in fn]
print(fns)

pdf_all = PdfFileMerger()
for i in fns:
    pdf_all.append(i)
with open(f'{Save_Path}合成后的.pdf','wb') as out:
    pdf_all.write(out)




# pdf_file = r'E:\TEMP\6TEST\GRRPA\huanchongqi\testpdf.pdf'
# pdf_file_c = r'E:\TEMP\6TEST\GRRPA\huanchongqi\testpdf_c.pdf'
# save_file = r'E:\TEMP\6TEST\GRRPA\huanchongqi\testpdf_1.pdf'

hg_dict = {}         # 2022-10-09 1/5   以'HYC' 或 'LB'开头的型号，不需要

doc = PdfFileReader(open(f'{Save_Path}合成后的.pdf', 'rb'))
# doc = PdfFileReader(open(file, 'rb'))


for i in range(doc.numPages):
    page = doc.getPage(i)
    txt = page.extract_text()
    try:
        txt_hg = txt.split('MFG.NO. ')[1].split('\n')[0]
        txt_model = txt.split('产品型号 MODEL ')[1].split(' ')[0]  # 2022-10-09 2/5  增加 产品型号
    except:
        print(i, txt_hg, txt)
        print('空白也面。')
        continue    # 2022-10-09 3/5   增加 去除空白页

    # print(txt_hg)
    # 2022-10-09 4/5   以'HYC' 或 'LB'开头的型号，不需要
    if txt_model.startswith('HYC') or txt_model.startswith('LB'):
        print(i, txt_hg,txt_model)
        continue
    else:
        hg_dict[i] = txt_hg
print(hg_dict)
input('--'*88)
    # weizhi = page.search_for("产品型号")
    # print(text)
    # print(page, i, weizhi)

# print(hg_list)

# hg_dict = dict(zip([x for x in range(len(hg_list))], hg_list)) # 2022-10-09 5/5 去掉
hg_dict_O = sorted(hg_dict.items(),key=lambda x:x[1],reverse=False)

# print(hg_dict)
# print(hg_dict_O)
hg_list_n = [k for k,v in hg_dict_O]
# print(hg_list_n)
pdf_writer = PdfFileWriter()
for i in hg_list_n:
    pdf_writer.addPage(doc.getPage(i))
# n_file = "排序后的.".join(file.split('.'))
with open(f'{Save_Path}合成排序后.pdf','wb') as out:
    pdf_writer.write(out)


from PyPDF2 import PdfFileMerger,PdfFileReader, PdfFileWriter
import os


Save_Path = 'E:\\TEMP\\6TEST\\GRRPA\\huanchongqi\\'
fns = [os.path.join(root, fn) for root, dirs, files in os.walk(Save_Path) for fn in files if 'ererer'  in fn]
print(fns)

pdf_all = PdfFileMerger()
for i in fns:
    pdf_all.append(i)
with open(f'{Save_Path}合成后的.pdf','wb') as out:
    pdf_all.write(out)




# pdf_file = r'E:\TEMP\6TEST\GRRPA\huanchongqi\testpdf.pdf'
# pdf_file_c = r'E:\TEMP\6TEST\GRRPA\huanchongqi\testpdf_c.pdf'
# save_file = r'E:\TEMP\6TEST\GRRPA\huanchongqi\testpdf_1.pdf'

hg_list = []

doc = PdfFileReader(open(f'{Save_Path}合成后的.pdf', 'rb'))
# doc = PdfFileReader(open(file, 'rb'))


for i in range(doc.numPages):
    page = doc.getPage(i)
    txt = page.extract_text()
    print(txt)

    try:
        txt_hg = txt.split('MFG.NO. ')[1].split('\n')[0]
        txt_rq = txt.split('MFG.DATE ')[1].split('\n')[0].replace('.', '-')  # 2022-10-08 1/3 增加日期
        txt_model = txt.split('产品型号 MODEL ')[1].split(' ')[0]  # 2022-10-08 1/3 增加日期
    except:
        print(i, txt_hg, txt_rq, txt_model)

    print(i, txt_hg, txt_rq, txt_model)
    input('--' * 88)
    hg_list.append([txt_hg, txt_rq])    # 2022-10-08 2/3 增加日期
    # weizhi = page.search_for("产品型号")
    # print(text)
    # print(page, i, weizhi)

# print(hg_list)

hg_dict = dict(zip([x for x in range(len(hg_list))], hg_list))
hg_dict_O = sorted(hg_dict.items(),key=lambda x:x[1],reverse=False)

# print(hg_dict)
# print(hg_dict_O)
hg_list_n = {k: v[1] for k, v in hg_dict_O}  # 2022-10-08  3/3 增加带有日期的字典
def dict_flip(dict_source):
    """
    反转字典
    :param dict_source: 原字典
    :return: 反转后的字典，相同值的添加为列表
    """
    dic_flipped = {}
    for k, v in dict_source.items():
        if v not in dic_flipped:
            dic_flipped[v] = [k]
        else:
            dic_flipped[v].append(k)
    return  dic_flipped


for k, v in dict_flip(hg_list_n).items():   # 2022-10-08  4/4
    print(k, v )
    pdf_writer = PdfFileWriter()
    for i in v:
        pdf_writer.addPage(doc.getPage(i))
    with open(f'{Save_Path}合成且排序_{k}.pdf', 'wb') as out:
        pdf_writer.write(out)


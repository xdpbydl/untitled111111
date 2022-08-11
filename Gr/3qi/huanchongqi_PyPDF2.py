from PyPDF2 import PdfFileMerger,PdfFileReader, PdfFileWriter
import os

Save_Path = 'E:\\TEMP\\6TEST\\GRRPA\\huanchongqi\\'
fns = [os.path.join(root, fn) for root, dirs, files in os.walk(Save_Path) for fn in files if ('ererer' and 'pdf') in fn]
print(fns)

# pdf_all = PdfFileMerger()
# for i in fns:
#     pdf_all.append(i)
# with open('merged.pdf','wb') as out:
#     pdf_all.write(f'{Save_Path}合成后的.pdf')




# pdf_file = r'E:\TEMP\6TEST\GRRPA\huanchongqi\testpdf.pdf'
# pdf_file_c = r'E:\TEMP\6TEST\GRRPA\huanchongqi\testpdf_c.pdf'
# save_file = r'E:\TEMP\6TEST\GRRPA\huanchongqi\testpdf_1.pdf'
for file in fns:
    hg_list = []

    # doc = PdfFileReader(open(f'{Save_Path}合成后的.pdf', 'rb'))
    doc = PdfFileReader(open(file, 'rb'))


    hg_new = []
    for i in range(doc.numPages):
        page = doc.getPage(i)
        txt = page.extractText()
        try:
            txt_hg = txt.split('MFG.NO. ')[1].split('\n')[0]
        except:
            print(i, txt_hg, txt)
        # print(txt_hg)
        hg_list.append(txt_hg)
        # weizhi = page.search_for("产品型号")
        # print(text)
        # print(page, i, weizhi)

    # print(hg_list)

    hg_dict = dict(zip([x for x in range(len(hg_list))], hg_list))
    hg_dict_O = sorted(hg_dict.items(),key=lambda x:x[1],reverse=False)

    # print(hg_dict)
    # print(hg_dict_O)
    hg_list_n = [k for k,v in hg_dict_O]
    # print(hg_list_n)
    pdf_writer = PdfFileWriter()
    for i in hg_list_n:
        pdf_writer.addPage(doc.getPage(i))
    n_file = "排序后的.".join(file.split('.'))
    with open(n_file,'wb') as out:
        pdf_writer.write(out)


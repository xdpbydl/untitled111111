import os


def kill_process(process):
    """
    杀进程
    :param process: 进程名
    :return:
    """
    os.system(f'taskkill /IM {process}')


# kill_process('cmd.exe')
#
# os.system('cd C:\\"Program Files"\\Google\\Chrome\\Application')


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
    return dic_flipped


aa = {7: '2021-12-28', 17: '2021-12-28', 8: '2021-12-29', 18: '2021-12-29', 9: '2021-12-29', 19: '2021-12-29', 56: '2022-08-12', 59: '2022-08-12',
      4:    '2022-08-12', 16: '2022-08-12', 5: '2022-08-12', 14: '2022-08-12', 3: '2022-08-12', 13: '2022-08-12', 6: '2022-08-12', 15: '2022-08-12',
      0: '2022-08-12', 11: '2022-08-12', 2: '2022-08-12', 12: '2022-08-12', 1: '2022-08-12', 10: '2022-08-12', 22: '2022-08-12', 34: '2022-08-12',
      36: '2022-08-12', 42: '2022-08-12', 37: '2022-08-12', 43: '2022-08-12', 20: '2022-08-12', 32: '2022-08-12', 21: '2022-08-12', 33: '2022-08-12',
      38: '2022-08-05', 24: '2022-08-05', 25: '2022-08-05', 39: '2022-08-05', 26: '2022-08-05', 27: '2022-08-05', 40: '2022-08-05', 28: '2022-08-05',
      29: '2022-08-05', 41: '2022-08-05', 30: '2022-08-05', 31: '2022-08-05', 60: '2022-07-01', 62: '2022-07-01', 61: '2022-07-01', 63: '2022-07-01',
      64: '2022-07-01', 23: '2022-08-12', 35: '2022-08-12', 44: '2022-08-12', 51: '2022-08-12', 65: '2022-08-12', 72: '2022-08-12', 45: '2022-08-12',
      52: '2022-08-12', 48: '2022-08-12', 53: '2022-08-12', 46: '2022-08-12', 54: '2022-08-12', 47: '2022-08-12', 55: '2022-08-12', 68: '2022-08-12',
      75: '2022-08-12', 69: '2022-08-12', 76: '2022-08-12', 70: '2022-08-12', 77: '2022-08-12', 71: '2022-08-12', 78: '2022-08-12', 67: '2022-08-12',
      74: '2022-08-12', 50: '2022-08-12', 58: '2022-08-12', 49: '2022-08-12', 57: '2022-08-12', 66: '2022-08-12', 73: '2022-08-12'}

# bb = dict_flip(aa)
# print(bb)




def get_newfile(Project_Path,f_name, new_path):
    """
    查看文件是否更新，有更新备份后覆盖文件
    :param Project_Path: 需要覆盖更新的路径
    :param f_name: 文件件名
    :param new_path: 获取的路径（可能会变更的）
    :return:
    """

    import hashlib, os, time, shutil
    riqi = time.strftime('%Y-%m-%d-%M-%S')
    old_file = f'{Project_Path}model\\{f_name}'
    new_file = f'{new_path}\\{f_name}'  # 远程文件
    old_bak = f'{Project_Path}model\\bak\\{f_name}{riqi}'


    def GetMD5FromLocalFile(filename):
        """
        Get local file's MD5 Info.
        @param filename:file path & file name
        @return:MD5 Info
        """
        file_object = open(filename, 'rb')
        file_content = file_object.read()
        file_object.close()
        file_md5 = hashlib.md5(file_content)
        return file_md5.hexdigest()

    # try:
    if GetMD5FromLocalFile(old_file) != GetMD5FromLocalFile(new_file):
        shutil.copyfile(old_file, old_bak)
        shutil.copyfile(new_file, old_file)
        print("文件有更新，备份、复制文件。")

    else:
        print("文件没有更新。")
    # except:
    # print("文件更新出错，可能文件不存在。")


# r'\\192.168.2.143\GRWL_PRA生成数据\对重块\\1对照表\\日立对重块 规格对照表.xlsx'  # 远程文件

import pandas as pd

file = r'E:\TEMP\Desktop\日立缓冲器标签.xlsx'

df = pd.read_excel(file)
# df.loc[df['产品代码'].str.contains('i-Search-02'), '备注'] = '成功'
# df = df.loc[df['箱头指令产出日期'].str.contains('i-Search-02')]
for i, r in df.iterrows():
    str1 = f"{r['箱头指令产出日期']}_{r['工号']}"
    str2 = f"{r[['箱头指令产出日期', '工号']]}"
    print(str1)
    print(str2)

    input('--'*88)
# f"{self.Save_Path}{self.pdf_name}_{pv_1[['箱头指令产出日期','工号']]}.pdf"
# f"{self.Save_Path}{self.pdf_name}_{pv_1['箱头指令产出日期']}_{pv_1['工号']}.pdf"

--df.to_excel(file,index=False)
# for  i in range(当一个NBA那个就是说。)
import hashlib, os, time, shutil

old_file = r'E:\TEMP\6TEST\GRRPA\duichongkuai\old\1.txt'
new_file = r'E:\TEMP\6TEST\GRRPA\duichongkuai\new\1.txt'  # 远程文件
old_bak = r'E:\TEMP\6TEST\GRRPA\duichongkuai\bak\1.txt'


def get_file_time(filename):
    mtime = time.ctime(os.path.getmtime(filename))
    ctime = time.ctime(os.path.getctime(filename))
    return [ctime, mtime]


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
#     if GetMD5FromLocalFile(old_file) != GetMD5FromLocalFile(new_file):
#         if get_file_time(new_file)[1] > get_file_time(old_file)[1]:
#             riqi = time.strftime('%Y-%m-%d')
#             shutil.copyfile(old_file, old_bak)
#             shutil.copyfile(new_file, old_file)
#             print("文件有更新，备份、复制文件。")
#         else:
#             print("old文件修改日期大于new文件。")
#     else:
#         print("文件没有更新。")
# except:
#     print("文件更新出错，可能文件不存在。")


def get_file_stauts(filename, time_n=60, time_s_e=["00:00:00", "23:59:59"]):
    """
    判断文件的，在time_s_e区间内，且小于time_n分钟内。
    :param filename: 文件的绝对路径、文件名
    :param time_n: 距离当前的分钟
    :param time_s_e: 文件的起始区间
    :return: 1  文件存在，在time_s_e区间内，且小于time_n分钟内； 0
    """
    now_t = time.time()
    now_localtime = time.strftime("%H:%M:%S", time.localtime())
    if os.path.exists(filename) and time_s_e[0] < now_localtime < time_s_e[1]:
        # mtime = time.ctime(os.path.getmtime(filename))
        print(os.path.getctime(filename))
        ctime = os.path.getctime(filename)
        if (now_t - ctime) / 60 < time_n:
            print(f'文件存在和当前时间相差{int((now_t - ctime) / 60)}分！小于{time_n}分。')
            return 1
        else:
            print(f'文件存在和当前时间相差{int((now_t - ctime) / 60)}分！超出{time_n}分。')
            now_t - ctime
            return 0
    else:
        print(f'文件不存在,或时间超过{time_s_e}区间！')
        return 0


file = r'E:\TEMP\6TEST\新建文本文档.txt'
get_file_stauts(file, time_s_e=["00:00:00", "08:00:00"])

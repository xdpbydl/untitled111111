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


try:
    if GetMD5FromLocalFile(old_file) != GetMD5FromLocalFile(new_file) :
        if get_file_time(new_file)[1] > get_file_time(old_file)[1]:
            riqi = time.strftime('%Y-%m-%d')
            shutil.copyfile(old_file, old_bak)
            shutil.copyfile(new_file, old_file)
            print("文件有更新，备份、复制文件。")
        else:
            print("old文件修改日期大于new文件。")
    else:
        print("文件没有更新。")
except:
    print("文件更新出错，可能文件不存在。")

def get_newfile(gv_File_Path, f_name, new_path):
    import hashlib, os, time, shutil
    riqi = time.strftime('%Y-%m-%d')
    old_file = f'{gv_File_Path}model\\{f_name}'  # MODEL下文件
    new_file = f'{new_path}\\{f_name}'  # 远程文件
    old_bak = f'{gv_File_Path}model\\bak\\{f_name}{riqi}'

    def get_file_time(filename):
        mtime = time.ctime(os.path.getmtime(filename))
        ctime = time.ctime(os.path.getctime(filename))
        # mtime = os.path.getmtime(filename)
        # ctime = os.path.getctime(filename)
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
    if GetMD5FromLocalFile(new_file) != GetMD5FromLocalFile(old_file):
        print(get_file_time(new_file)[1], get_file_time(old_file)[1], get_file_time(new_file)[1] > get_file_time(old_file)[1])
        if get_file_time(new_file)[1] > get_file_time(old_file)[1]:
            shutil.copyfile(old_file, old_bak)
            shutil.copyfile(new_file, old_file)
            print("文件有更新，备份、复制文件。")
        else:
            print("old文件修改日期大于new文件。")
    else:
        print("文件没有更新。")
    # except:
    # print("文件更新出错，可能文件不存在。")


get_newfile('E:\\TEMP\\6TEST\\GRRPA\\duichongkuai\\', '接单_物料对应分类.xlsx', 'e:\\')
# r'\\192.168.2.143\GRWL_PRA生成数据\对重块\\1对照表\\日立对重块 规格对照表.xlsx'  # 远程文件

logfile = r'c:\11\txt.txt'
path_1 = 'E:\\TEMP\\6TEST\\GRRPA\\duichongkuai\\'
file_n = '接单_物料对应分类.xlsx'
if 1:
    logfile += f',{path_1}{file_n}'
    print(logfile)

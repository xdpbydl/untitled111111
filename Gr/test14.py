import os
import shutil

scr_file = r'C:\Users\Administrator\Desktop\grwl_log\000'
other_file = r'C:\Users\Administrator\Desktop\grwl_log\111'

txt_file = r'__本次操作完成__.txt'


def copy_file(scr_file, trg_file, iscopy_dir=0, ismove_file=0):
    # iscopy_dir 为0，不复制目录，为1，复制目录；
    # ismove_file为0，只复制文件，为1，移动文件。
    source_path = os.path.abspath(scr_file)
    target_path = os.path.abspath(trg_file)
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    if os.path.exists(source_path):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(source_path):
            for file in files:
                # 只复制源文件夹里的文件
                # src_file = os.path.join(root, file)
                src_file = os.path.join(scr_file, file)
                if os.path.exists(src_file):
                    if ismove_file:
                        shutil.move(src_file, target_path)
                    else:
                        shutil.copy(src_file, target_path)
                    print(src_file,  '*1' * 8)

            if iscopy_dir:
                for dir in dirs:
                    if not os.path.exists(target_path + '\\' + dir):
                        src_dir = os.path.join(root, dir)
                        target_path_1 = target_path + '\\' + dir
                        print(src_dir + '*2' * 8 + target_path_1)
                        shutil.copytree(src_dir, target_path_1)

                    else:
                        print(dir + '该文件夹已存在，无法复制')


# 创建TXT文件
with open(scr_file + '\\' + txt_file, 'w') as file1:
    file1.close()

def dir_file(scr_file):
    # 当天第一次成功生成文件，copy到文件夹【1】下，依次类推
    scr_file_1 = scr_file
    for i in range(1, 99):
        if os.path.isfile(scr_file_1 + '\\' + txt_file):
            scr_file_1 = scr_file + '\\' + str(i)

        else:
            return scr_file_1


# 多次生成，复制到其他目录下
# try:
#     copy_file(scr_file, dir_file(scr_file), iscopy_dir=0, ismove_file=1)
# except:
#     pass

# 复制到远程目录

# copy_file(scr_file, other_file, iscopy_dir=1)
copy_file(scr_file, dir_file(other_file), iscopy_dir=1, ismove_file=0)

print('copy files finished!')

from PIL import Image
import os, shutil


def get_outfile(infile, outfile='', t_str='change'):
    """
    根据源文件，输出 目标目录路径，及文件
    :param infile: 源照片文件
    :param outfile: 目标目录路径
    :param t_str: 目标目录下子目录
    :return: outfile        标目录路径，及文件
    """
    dir, suffix = os.path.split(infile)
    if outfile != '':
        dir = outfile
    outfile = f'{dir}\\{t_str}\\{suffix}'
    try:
        os.makedirs(f'{dir}\\{t_str}')
    except:
        pass
    return outfile


def resize(path, out_path='', factor=0.9):
    """
    调整照片大小
    path， 照片的路径
    out_path， 输出文件路径
    factor，缩放的比例～
    """
    out_path_x = get_outfile(path, out_path)
    try:
        img = Image.open(path)
    except:
        print(f"{'^' * 10}{path},文件可能不为图片！{'^' * 10}")
        return
    x, y = img.size
    while factor > 0:
        x_change, y_change = tuple(map(lambda x: int(x * factor), img.size))
        factor -= 0.1
        # print(factor, x, y)
        if x < 200 or y < 200:
            print(f"{'-' * 10}{path},文件尺寸小于200！{'-' * 10}")
            out_path_a = get_outfile(path, out_path, t_str='small')
            shutil.copyfile(path, out_path_a)
            return
        elif 800 >= x > 200 and 800 >= y > 200 and 600 >= os.path.getsize(path) / 1024:
            print(f"{'@' * 10}{path},文件尺寸及文件大小正合适.{'@' * 10}")
            # print(00 >= x > 200 , 800 >= y > 200 , 600 >= os.path.getsize(path) / 1024)
            # print(path, out_path_x)
            shutil.copyfile(path, out_path_x)
            return
        elif 800 >= x_change > 200 and 600 >= y_change > 200:
            try:
                out = img.resize((x_change, y_change), Image.ANTIALIAS)
            except:
                print(f"{'=' * 10}{path},文件转换错误,请检查！！！{'=' * 10}")
                out_path_b = get_outfile(path, out_path, t_str='ERROR')
                shutil.copyfile(path, out_path_b)
                return
            out.save(out_path_x)
            if 600 <= os.path.getsize(out_path_x) / 1024:
                continue
            return


# resize(r'E:\TEMP\6TEST\qqq.png')
file_dir = r'E:\TEMP\6TEST\yz_temp\21年9月新增老师'
to_dir = r'E:\TEMP\6TEST\yz_temp\3老师及职工'

# for i in os.listdir(file_dir):
#     # if os.path.isfile(os.path.join(file_dir, i)):   # 不遍历子目录
#     #     resize(os.path.join(file_dir, i), to_dir)


i = 0
for (root, dirs, files) in os.walk(file_dir):
    for filename in files:
        # 遍历所有文件，包括子目录
        # print(os.path.join(root, filename))
        resize(os.path.join(root, filename), to_dir)
        i += 1
    print(i)
    for dirc in dirs:
        print(os.path.join(root, dirc))


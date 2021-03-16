from PIL import Image
import os


def compress_image(infile, outfile='', mb=150, step=10, quality=60):
    """不改变图片尺寸压缩到指定大小
    :param infile: 压缩源文件
    :param outfile: 压缩文件保存地址
    :param mb: 压缩目标，KB
    :param step: 每次调整的压缩比率
    :param quality: 初始压缩比率
    :return: 压缩文件地址，压缩文件大小
    """

    def get_size(file):
        return os.path.getsize(file) / 1024

    def change_size(infile, quality):
        im = Image.open(infile)
        im.save(infile, quality=quality)

    o_size = get_size(infile)
    if o_size <= mb:
        return infile
    if not outfile:
        dir, suffix = os.path.splitext(infile)
        outfile = '{}-out{}'.format(dir, suffix)
    while o_size > mb:
        print(o_size, quality, outfile)
        change_size(outfile, quality=quality)
        # input('___')
        if quality - step < 0:
            break
        quality -= step
        o_size = get_size(outfile)

    return outfile, get_size(outfile)


compress_image(r'E:\TEMP\6TEST\qqq.png', mb=60, step=10, quality=40)

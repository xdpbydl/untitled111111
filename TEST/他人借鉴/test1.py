from PIL import Image
import os, shutil, time, datetime

# path = r'E:\TEMP\Desktop\李志忠G445302200608173316.png'
# # path = r'E:\TEMP\Desktop\copy_123.jpg'
# path1 = r'E:\TEMP\Desktop\121.png'
# out_path_x = r'E:\TEMP\Desktop\out.png'
# # img = Image.open(r'E:\TEMP\Desktop\李志忠G445302200608173316.png')
#
# img1 = Image.open(path1)
#
# img2 = Image.open(path)
#
# img1.save(out_path_x)


a = '06:01'
b = '6:05'
# t = time.strptime(a, '%H:%M')

time_a = datetime.datetime.strptime(a, '%H:%M')
time_b = datetime.datetime.strptime(b, '%H:%M')
print(time_b, time_a)

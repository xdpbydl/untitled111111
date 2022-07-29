import os


srcFile = 'E:\\TEMP\\3Note\\截图\\'
fns = [os.path.join(root, fn) for root, dirs, files in os.walk(srcFile) for fn in files if 'Snipaste_2022' and '49' in fn]
print(fns)
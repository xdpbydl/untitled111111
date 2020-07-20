import re

tt = '''
对重块
1040×150×67,
35kg/块_合成 13510603
WORK作业
1040×1501×67
1040×1502×67
1040×1503×67
1040×1504×67
1040×1505×67
'''
guige = re.findall(r'\n\b对重块\b\n.*\n.*\n.*\n.*\n', tt)
guige1 = re.findall(r'\d{1,}×\d{1,}×\d{1,}', str(guige))

print('#', end="")
print(1, end="")
print(2, end="")
print(3)
print(guige1)


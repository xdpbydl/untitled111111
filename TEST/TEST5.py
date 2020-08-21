import wmi,re

# c = wmi.WMI()
#
# for process in c.Win32_Process():  # 这里枚举所有进程
#     # print (process.ProcessId, process.Name)
#     # print (process.Name, "\n")
#     pass

# for process in c.Win32_Process(name="cmd.exe"):
#     print(process.ProcessId, process.Name)
#     process.Terminate()


# print([5 for i in range(10)])
#
#
# a = [1,2,3,4,5,6,7,8,9]
# print(a[1::2])
#
# print(1, 2, 3, sep=':')
# print(5&3, 5%4)
#
# print(globals())
# print(locals())

x = {1: 2}
x[1] = 49
print(x)
print([i for i in range(1000) if i % 114 == 0])

print([index for index, value in enumerate([3, 5, 7, 3, 7]) if value == max([3, 5, 7, 3, 7])])
#  [2, 4]

x = [3, 5, 3, 7]
print([x.index(i) for i in x if i == 3])
# [0, 0]

vec = [[1, 2], [3, 4]]
print([col for row in vec for col in row])
#  [1, 2, 3, 4]
print([[row[i] for row in vec] for i in range(len(vec[0]))])
#  [[1, 3], [2, 4]]

print(abs(3 + 4j))
print(abs(1 + 2j))

c1 = 12 + 0.2j
print("c1Value: ", c1)
print("c1Type", type(c1))

c2 = 6 - 1.2j
print("c2Value: ", c2)

#  对复数进行简单计算
print("c1+c2: ", c1+c2)
print("c1*c2: ", c1*c2)
# (a+bj)(c+dj)=(ac-bd)+(bc+ad)j    (6*12+1.2*0.2)-(0.2*6 - 12*1.2)

print('The first:{1}, the second is {0}'.format(65, 97))
#  The first:97, the second is 65

print('{0:#d},{0:#x},{0:#o}'.format(65))
print('a'.join('abc'.partition('a')))
print('abc'.partition('a'))
#  ('', 'a', 'bc')

print(''.join(re.split('[sd]','asdssfff')))
print(re.split('[sd]','asdssfff'))
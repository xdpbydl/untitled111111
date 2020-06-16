import re

test = 'woere%jpg'
print(re.split(r'%', test))

test = 'woere.jpg'
print(re.split('\.', test))        # .需要转义？？


aList = [1,2,3]
bList = ['www', 'pythontab.com']
aList.append(bList)
print(aList)
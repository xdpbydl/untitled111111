import re

string = "GRFⅡ35.12-100"
aa = re.findall(r"(\d+\.?\d*)-", string)
print(type(str(aa)))
print(aa[0])

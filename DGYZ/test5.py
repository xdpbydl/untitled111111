import ast

# txt = '''{"css-selector":"body>div>div>div>div>div>h3>a","xpath":"//*[@id=\"%s\"]/h3[1]/a[1]"}'''%(1)
# # txt = {"css-selector":"body>div>div>div>div>div>h3>a","xpath":"//*[@id='1']/h3[1]/a[1]"}
# print(txt)
# test_dict = ast.literal_eval(txt)
# print(txt)

for i in range(1, 11):
    # 鼠标点击
    # attrMap = '''{"css-selector":"body>div>div>div>div>div>h3>a","xpath":"//*[@id="{i}"]/h3[1]/a[1]"}'''.format(i=i)
    attrMap = '''{"css-selector":"body>div>div>div>div>div>h3>a","xpath":"//*[@id\\"%s\\"]/h3[1]/a[1]"}'''%(i)
    print(attrMap)
    print(type(attrMap))
    attrMap = ast.literal_eval(attrMap)
    print(attrMap)
    # print(type(attrMap))

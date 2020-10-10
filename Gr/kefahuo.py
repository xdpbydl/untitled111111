import pandas as pd
import os, re
from shutil import copyfile
import numpy as np

file = r'E:\TEMP\02GR\kefahuo\可发货通知单报表.xls'
model_file = r'E:\TEMP\02GR\kefahuo\model\可发货通知书(代运）2020——导入2.0_1.xlsx'
im_file = r'E:\TEMP\02GR\kefahuo\可发货通知书(代运）2020——导入2.0______1.xlsx'
save_file = r'E:\TEMP\02GR\kefahuo\11.xls'
zhiqian_file = r'E:\TEMP\02GR\kefahuo\物流直签.xlsx'

if os.path.exists(im_file):
    os.remove(im_file)
    copyfile(model_file, im_file)
else:
    copyfile(model_file, im_file)

df = pd.read_excel(file, index=False)
im_df = pd.read_excel(im_file, index=False)

# print(df)
# 分列'层/站/门/高']          [['层', '站', '门', '高']]
# print(df)

df1 = df['层/站/门/高'].str.split('/', expand=True)
df1.columns = ['层', '站', '门', '高']
df = df.join(df1)
df.drop(['层/站/门/高'], axis=1, inplace=True)
# df.explode('层/站/门/高')
# ret_df = pd.DataFrame([i for i in df[df.columns['层/站/门/高']].str.split("/")], columns=df.columns['层/站/门/高'].split("/"))
# print(ret_df)
# df1 = df.drop('层/站/门/高', axis=1).join(
#     df['层/站/门/高'].str.split('/', expand=True).stack().reset_index(level=1, drop=True).rename('层/站/门/高'))
# print(df1)

# 以下修改,不提示警告
pd.set_option('mode.chained_assignment', None)
# # '运输商'列值为'客户自理'开始的,'送货方式'列值改为'自提'
# df.送货方式[df['运输商'].str.contains('^客户自理')] = '自提'
# # '运输商'列值为  非（ '客户自理',‘广州广日物流有限公司’），'送货方式'列值改为'自运'
# yunshus = ['广州广日物流有限公司', '客户自理']
# df.送货方式[~df['运输商'].str.contains('|'.join(yunshus))] = '自运'


# 筛选"运输商" ,为'广州广日物流有限公司'的
df = df[df['运输商'].str.contains('广州广日物流有限公司')]

# print(df.电梯工号)
df = df.applymap(str)
# print(im_df.总工号)
#
# print(im_df.columns)
# print(df.columns)

col_d = {"型号": "电梯型号",
         "层": "层",
         "站": "站",
         "门": "门",
         "订货单位": "签订单位",
         "使用单位": "项目名称",
         "提升高度": "高",
         "营业员": "业务员",
         "安装地址": "送货地点",
         "总工号": "电梯工号"}
for key in col_d:
    im_df[key] = df[col_d[key]]
    # print(key)
    # print(col_d[key])

col_e = {"交货要求": "整梯",
         "合同库运费": 0,
         "实收运费": 0,
         "广日合同标准价": 0,
         "制表人": "陈家荣",
         "制表日期": "20200101",
         "收支状态": "正常"}
for key in col_e:
    im_df[key] = col_e[key]

print(im_df.倾角)
# if im_df['层'] == 0 and im_df['站'] == 0 and im_df['门'] == 0:
#     print(im_df['型号'], im_df['层'], im_df['站'], im_df['门'])
# df.a = df.a.where(df.a > 0.5, (1 / df.a) * (-1))
# im_df.倾角 = im_df.where[]apply
# im_df.总工号 = df.电梯工号
# im_df.收支状态 = r'正常'

# im_df.倾角 = im_df.型号.where((im_df[u'层'] == '0') & (im_df[u'站'] == '0') & (im_df[u'门'] == '0'))
# im_no = re.findall(r"(\d+\.?\d*)-", im_df.型号)[0]
# lm_no = re.findall(r"(\d+\.?\d*)-", "GRFⅡ35.12-100")[0]
# im_df.倾角 = np.where((im_df[u'层'] == '0') & (im_df[u'站'] == '0') & (im_df[u'门'] == '0'), "GRFⅡ35.12-100", '0')
# im_df.倾角=[x for  x  in re.split(' ',an) if str(x) !='' and str(x).find('东')!=-1]


# 层站门均为0时把型号字段中-前面的数字（数字可能有整数，有小数点）填充到倾角字段中
im_df.倾角 = np.where((im_df[u'层'] == '0') & (im_df[u'站'] == '0') & (im_df[u'门'] == '0'), im_df.型号, '0')



print(im_df.倾角)


def re_1(i):
    if i != 0 and i != '0':
        res = re.findall(r"(\d+\.?\d*)-", i)[0]
        return res
    else:
        return 0

im_df.倾角 = im_df.倾角.apply(re_1)

#  ，把旧值的层 站 门 ，都为0，高赋值给新值, 不为0的，赋值空
im_df.提升高度 = np.where((im_df[u'层'] == '0') & (im_df[u'站'] == '0') & (im_df[u'门'] == '0'), im_df.提升高度, '')


# if (df.层 == '0' & df.站 == '0' & df.门 == '0'):
#     im_df.提升高度 = df.高
# else:
#     im_df.提升高度 = ''

# im_df.提升高度 = df.apply(lambda x: x.高 if (x.层 == '0' & x.站 == '0' & x.门 == '0') else '')
# where(df.层 == '0' & df.站 == '0' & df.门 == '0')
# df['ExtraScore'] = df['Nationality'].apply(lambda x: 5 if x != '汉' else 0)

print(im_df.倾角)
im_df.合同号 = im_df.总工号.str[:6]
im_df.工号 = im_df.总工号.str[-5:]
im_df.层站门 = im_df.层 + "/" + im_df.站 + "/" + im_df.门
# print(im_df.层 + "/" + im_df.站 + "/" + im_df.门 + " " + im_df.提升高度)
# print(im_df[['总工号', '合同号', '工号']])
# im_df.型号, im_df.层, im_df.站, im_df.门, im_df.订货单位, im_df.使用单位, im_df.营业员, im_df.安装地址 =
# im_df.型号, im_df.层, im_df.站, im_df.门 = df.电梯型号, df.层, df.站, df.门

# "交货要求"\"合同库运费"\实收运费"\"广日合同标准价"\"制表人"\"制表日期", 分别为"整体"\"0"\"0"\"0"\"陈家荣"\当前日期;

# "型号"\"层"\"站"\"门"\"订货单位"\"使用单位"\"营业员"\"安装地址" = "电梯型号"\"层"\"站"\"门"\"签订单位"\"项目名称"\"业务员"\"送货地址"


# 筛选【签订单位】为'广州广日电梯工程有限公司'的，把【收支状态】改为"物流直签"；
im_df.收支状态[im_df['订货单位'].str.contains('广州广日电梯工程有限公司')] = '物流直签'
#  把“物流直签”的，另存为一张表。
wuliuzhiqian = im_df[im_df['订货单位'].str.contains('广州广日电梯工程有限公司')]

# 把导出表，【订货单位】为“广州广日电梯工程有限公司”的，剔除。
im_df = im_df[~im_df['订货单位'].str.contains('广州广日电梯工程有限公司')]

df.to_excel(save_file, index=False)
im_df.to_excel(im_file, index=False)
wuliuzhiqian.to_excel(zhiqian_file, index=False)
# print(df)

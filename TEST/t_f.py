import pandas as pd
import numpy as np
import os

na = np.nan
file = r'E:\TEMP\6TEST\GRWL\P934\箱头指令产出GRWL8888880.xlsx'
save_file = r'E:\TEMP\6TEST\GRWL\P934\test_grwltj.xlsx'
save_file_1 = r'E:\TEMP\6TEST\GRWL\P934\test_grwltj_1.xlsx'
df_gr = pd.read_excel(file)

# df_gr.loc[df_gr['包装物编码'].str.contains('X151000985'), '包装物规格'] = '1700*550*500'
df_gr.loc[(df_gr['包装物编码']=='X151000985')&((df_gr['包装物规格'].isna()==True)|(df_gr['包装物规格'].isna()==True)), '包装物规格'] = '1700*550*500'   #会导致无法判断？？
# df_gr.loc[df_gr['包装物编码']=='X151000985', '包装物规格'] = '1700*550*500'
df_gr = pd.DataFrame(df_gr)
df_gr.to_excel(save_file_1)
# df = pd.DataFrame()
#
# # 判断是否有此字符内容
# z_bitname = 'P934箱头计划下达'
# # 导出生成Excel文件名
# z_Excelname = 'P934箱头指令明细箱头计划下达.xlsx'
#
pd.read_excel(save_file_1,header=False)
# allxlsPlan = []
#
# # 判断是否有此字符内容
# for w in range(len(lv_readyExcellist)):
#     if str(z_bitname) in lv_readyExcellist[w]:
#         print(lv_readyExcellist[w])
#         allxlsPlan.append(lv_readyExcellist[w])
#
# if len(allxlsPlan) > 0:
#
#     for w in range(len(allxlsPlan)):
#         if str(z_bitname) in allxlsPlan[w]:
#             filePath = allxlsPlan[w]
#             print('-----路径---')
#             print(filePath)
#
#             # ---------------------------先处理规格问题   1
#             print('---------------先处理规格问题--------------')
#             lists = filePath.split('/')
#             dltable = pd.read_excel(filePath, sheet_name='Sheet1')
#             # 指定在 包装物材质（索引：26） 列前面新插入 包装物规格列
#             new_col = dltable['包装物名称'].str.split('_', expand=True)[1]
#             dltable.insert(loc=26, column='包装物规格', value=new_col)
#             # 替换 *
#             dltable['包装物规格'] = dltable['包装物规格'].str.replace('*', '×')
#             # 是否出现这种格式：轿顶箱_木箱，是 包装物规格 则变为空值
#             dltable['包装物规格'] = dltable['包装物规格'].mask(dltable['包装物规格'].str.contains(r'×', na=True) != True, '')
#             # 替换 X
#             dltable['包装物规格'] = dltable['包装物规格'].str.replace('×', '*')

              # 2021-09-03 【包装物编码】列为'X151000985'，且【包装物规格】列为空的，修改【包装物规格】列为1700*550*500
#             dltable.loc[(dltable['包装物编码']=='X151000985')&(dltable['包装物规格'].isna()==True), '包装物规格'] = '1700*550*500'

#             Furl = os.path.join(r'C:/RPA/Project/GRWL_p934duizhanminxi/GRWL20/GR/publicexcel', str(lists[len(lists) - 1]))
#             dltable = pd.DataFrame(dltable)
#             dltable.to_excel(Furl, index=False)
#             print('-----------规格处理--------保存成功')
#
#             # ----------------------------重新-读取 excel，准备合并   2
#             dfc = pd.read_excel(filePath, sheet_name='Sheet1')
#             # print('-------打印 df-------')
#             df = pd.concat([df, dfc], axis=0, ignore_index=True)
#
#     print('-------打印 df-------')
#     print(df)
#
#     print('-------导出-------')
#     Fileurl = os.path.join(lv_HuiZongExcelurl, str(z_Excelname))
#     # 转换成DataFrame
#     df = pd.DataFrame(df)
#     df.to_excel(Fileurl, index=False)
#     print('-------附件路径-------')
#     print(Fileurl)
#
#     # 操作日志记录
#     if len(df) > 0:
#         lv_4huicount = 1
#         self.gv_logoErrey = self.gv_logoErrey + '--导出P934箱头指令明细箱头计划下达汇总合并完成了哈----'
#         print('------------------导出P934箱头指令明细箱头计划下达汇总合并完成了哈-----------------')
#     else:
#         lv_4huicount = 0
#         self.gv_logoErrey = self.gv_logoErrey + '--导出P934箱头指令明细箱头计划下达汇总合并完成了哈----'
#         print('------------------导出P934箱头指令明细箱头计划下达汇总合并失败哈-----------------')
#
# else:
#     self.gv_logoErrey = self.gv_logoErrey + '--汇总-计划下达没有数据需合并----'

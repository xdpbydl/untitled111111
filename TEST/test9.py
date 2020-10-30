import pandas as pd

export_file = r'C:\Users\Administrator\Desktop\grwl_20201214\test.xlsx'
excel_data = pd.read_excel(export_file, index=False)
aa = excel_data.columns.tolist()
# print(aa)

# print(aa[1:]+ [aa[0]])
if excel_data.columns[0] == 'eeeee':
    print("---")
    excel_data.columns = aa[1:] +  ['']

# df.loc[:, ~df.columns.str.contains('Unnamed')]
# excel_data.loc[:, ~excel_data['运输商'].astype(str).contains('广州广日物流有限公司')] = "自提"

excel_data['运输商'] = excel_data['运输商'].astype(str)

# ['运输商']列非'广州广日物流有限公司'的数据，【'送货方式'】列改为'自提'
excel_data.loc[~excel_data['运输商'].str.contains('广州广日物流有限公司'), '送货方式'] = '自提'
excel_data.loc[excel_data['运输商'].str.contains('广州广日物流有限公司'), '送货方式'] = '送货'
print(excel_data)

excel_data.to_excel(export_file, index=False)



if excel_data.iloc[0,1] == "没查询到任何数据！":

    print("发货单计划，没有数据!")
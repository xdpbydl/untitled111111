import pandas as pd
import numpy as np

# df = pd.DataFrame({'a': np.random.randn(6),
#                    'b': ['foo', 'bar'] * 3,
#                    'c': np.random.randn(6)})
#
#
# def my_test(a, b):
#     return a + b
# print(df)
#
# df['Value'] = df.apply(lambda row: my_test(row['a'], row['c']), axis=1)
# print(df)



te = pd.read_excel('TEST.xlsx', index=False)


# print(te)
# te.duplicated()
import pandas as pd
data=pd.DataFrame({'产品':['A','A','A','A'],'数量':[50,50,30,30]})
# if data.duplicated:
#     dataA=data.drop_duplicates().reset_index(drop=True)
# dataA=data.drop_duplicates()

print(data.duplicated())
# print(dataA)
# dataB=dataA.groupby(by='产品').agg({'数量':sum})
# print('数据汇总结果:')
# print(dataB)
#
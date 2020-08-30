import pandas as pd

data = pd.DataFrame({'ct': [1, 1, 2, 2, 3], '1_tf': [10, 20, 30, 40, 50]})
# co_1f_dict = data.groupby('ct')['1_tf'].sum().to_dict()
co_1f_dict = data.groupby('ct')['1_tf'].mean().to_dict()

a = data['ct'].reset_index(drop=True)
# print(a)

print(a.iloc[0])

print(co_1f_dict[a.iloc[0]])
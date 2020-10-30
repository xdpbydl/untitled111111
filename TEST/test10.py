import pandas as pd

df = pd.DataFrame({'A': ['bob', 'sos', 'bob', 'sos', 'bob', 'sos', 'bob', 'bob'],
                   'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
                   'C': [3, 1, 4, 1, None, 9, 2, 6],
                   'D': [1, 2, 3, 4, 5, 6, 7, 8]})

grouped = df.groupby('A')

print(grouped.count())
for name, group in grouped:
    print(name)
    print(group)
'''
bob
     A      B    C  D
0  bob    one  3.0  1
2  bob    two  4.0  3
4  bob    two  NaN  5
6  bob    one  2.0  7
7  bob  three  6.0  8
sos
     A      B    C  D
1  sos    one  1.0  2
3  sos  three  1.0  4
5  sos    two  9.0  6
         A      B     C  D
'''

# d = grouped.apply(lambda x: x.describe())


def fill_none(one_group):
   return one_group.fillna(one_group.mean()) # 把平均值填充到空值里面


d = grouped.apply(fill_none)
print(d)
'''
A                         
bob 0  bob    one  3.00  1
    2  bob    two  4.00  3
    4  bob    two  3.75  5
    6  bob    one  2.00  7
    7  bob  three  6.00  8
sos 1  sos    one  1.00  2
    3  sos  three  1.00  4
    5  sos    two  9.00  6
'''
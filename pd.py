import pandas as pd
import numpy as np
from pandas import Series, DataFrame

# print("dlfdk")
obj = pd.Series([3, 4, 5, -1.2, 1])
# print(obj)
# print(obj.values)
# print(obj.index)

obj2 = pd.Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
# print(obj2, obj2.index)

obj2['d'] = 6
# print(obj2[['c', 'a', 'd']])
# print(obj2[['a', 'b']])

# print(obj2[obj2 > 0])
# print(obj2 * 2)

print(np.exp(obj2))
print('b' in obj2, "e" in obj2)

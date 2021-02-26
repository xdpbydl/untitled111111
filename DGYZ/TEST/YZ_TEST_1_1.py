import re
import random

import pandas as pd

"""
【Python】自动化：Excel分组排序着色
需求：将包含['深圳','广州','惠州','东莞']字段分组，排序，并着色

tips:  需要导入 jinja2 包
"""

file = r'E:\TEMP\6TEST\test{}.xlsx'
df = pd.read_excel(file.format(1))

x = pd.Index(['深圳', '广州', '东莞', '北京'])
rule = '|'.join(x)
df['地区_rule'] = df['地区'].str.extract(f'({rule})')
df['地区_rule'] = df['地区_rule'].astype("category")
df['地区_rule'] = df['地区_rule'].cat.set_categories(x)
df.sort_values('地区_rule', inplace=True)
df.drop(columns='地区_rule', inplace=True)

rule_re = re.compile(rule)
colors = ['red', 'yellow', 'purple', 'pink', 'green', 'blue', 'brown', 'maroon']
random.shuffle(colors)


def match_rule(s):
    search = rule_re.search(s)
    if search:
        city = search.group()
        color = colors[x.get_loc(city)]
        return f'background-color: {color}'
    else:
        return ''


df_style = df.style.applymap(match_rule, subset=['地区'])
df_style.to_excel(file.format(2))

import pandas as pd

#沪市前面加0，深市前面加1，比如0000001，是上证指数，1000001是中国平安
# http://api.money.126.net/data/feed/1159949,1000625

def get_daily(code):
    url = f"http://api.money.126.net/data/feed/{code}"
    df = pd.read_csv(url, encoding="gb2312")
    return df

def get_code():
    pass

print(get_daily('1159949,1000625'))
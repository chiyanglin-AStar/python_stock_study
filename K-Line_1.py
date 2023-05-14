import requests
import json
import pandas as pd
import matplotlib
import pandas_datareader as web # 下載股票資料
import matplotlib.pyplot as plt # 基本畫圖
import mplfinance as mpf # 畫k線
import talib # 計算技術指標

# 導入pandas、matplotlib、mplfinance模組，將mplfinance模組縮寫為mpf
# 這邊要導入matplotlib的原因是因為mplfinance繪圖時需要調用mptplotlib模組
from matplotlib.gridspec import GridSpec # 畫圖網格佈局

# 下載股票資料
#df = web.DataReader('2330.TW', 'yahoo')

url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20210801&stockNo=0050"
payload = {}
headers = {}
response = requests.request("GET",url,headers=headers,data=payload)
print(response.text)

# 從1到12月
for m in range(2,3):
    url = "https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=2020{0:02d}01&stockNo=0050".format(m)
    print(url)

    # 取得股票資料json字串
    response = requests.get(url, headers=headers)
    print(response.text)

    # 從json字串轉為python的字典格式
    json_data = json.loads(response.text)
    datas = json_data["data"]
    fields = json_data["fields"]

# 存成Pandas的Dataframe
month_df = pd.DataFrame(datas, columns=fields)
year_df = pd.DataFrame(datas, columns=fields)

# 合併於整年的Dataframe
year_df = year_df.append(month_df, ignore_index=True)

# 轉成csv檔
year_df.to_csv("./year_stock.csv", encoding="big5")


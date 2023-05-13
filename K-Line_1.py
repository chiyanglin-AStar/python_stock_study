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

target_stock = '0050' #設定要繪製走勢圖的股票

#df = pd.read_csv(f'./data/{target_stock}.csv', parse_dates=True, index_col=1) #讀取目標股票csv檔的位置
df = pd.read_csv(f'./year_stock.csv', encoding="big5" , parse_dates=True, index_col=1) #讀取目標股票csv檔的位置

# 計算技術指標
sma = [20, 60, 120]
for i in sma:
    df['sma'+str(i)] = talib.SMA(df['Close'], i) # talib.SMA計算簡單平均

# 轉換index
df.index = df.index.format(formatter=lambda x: x.strftime('%Y%m%d')) # 簡化x軸顯示

# 開新一個畫布 
fig = plt.figure(figsize=(15, 5)) # 寬15 長5
gs = GridSpec(2, 1) # 設立2x1的網格

# 設定網格及子圖
ax = plt.subplot(gs[0, :]) # 子圖ax在網格的[0, 全部]
ax2 = plt.subplot(gs[1, :]) # 子圖ax在網格的[1, 全部]

# k線
mpf.candlestick2_ochl(ax,
                      df['Open'],
                      df['Close'],
                      df['High'],
                      df['Low'],
                      width=0.6, alpha=0.9,
                      colorup='r', colordown='g')

# 扣抵值 # sma
sma = [20, 60, 120]
for i in sma:
    ax.plot(df.index, df['sma'+str(i)], label='sma'+ str(i)) # 均線
    x, y = df.index[-i], df['Close'].iloc[-i]*0.98
    ax.plot(x, y, 'o', label=None) # 扣抵

ax.legend(loc=2, fontsize=15) # 顯示子圖的圖例

# x軸
leng = 130 # x軸頻率 以130筆資料顯示一個x標籤
ax.set_xticks(range(0, len(df.index), leng)) # x軸頻率
ax.set_xticklabels(df.index[::leng]) # 把index放進x軸
ax.set_xlim(0, len(df.index)) # 限制x軸範圍

# y軸
ax.set_ylim(min(df['Low']) * 0.95, max(df['High']) * 1.05) # 限制y軸範圍
ax.set_title('2330.TW', fontsize=30) # 設定子圖title fontsize:大小

# 顯示格線
ax.yaxis.grid(linestyle='-.', linewidth=0.5, color='gray', alpha=0.4) # linestyle:線樣式 linewidth:粗度 
ax.xaxis.grid(linestyle='-.', linewidth=0.5, color='gray', alpha=0.4) # color:顏色 alpha:透明度
ax2.yaxis.grid(linestyle='-.', linewidth=0.5, color='gray', alpha=0.4) # linestyle:線樣式 linewidth:粗度 
ax2.xaxis.grid(linestyle='-.', linewidth=0.5, color='gray', alpha=0.4) # color:顏色 alpha:透明度ㄑ

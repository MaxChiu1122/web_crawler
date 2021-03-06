import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_html('https://rate.bot.com.tw/xrt/quote/l6m/JPY')
item = int(input('請輸入要查詢的項目：\n 1 現金-本行買入 \n 2 現金-本行賣出 \n 3 即期-本行買入 \n 4 即期-本行賣出\n輸入數字: '))
days = int(input('請輸入要取得的最近樣本天數(2~120): '))
rate = df[0]
rate = rate.iloc[:,0:6]
rate.columns = ['掛牌日期','幣別','現金-本行買入','現金-本行賣出','即期-本行買入','即期-本行賣出']
rate_new = rate.iloc[:days,[0,item+1]]
rate_new['掛牌日期'] = pd.to_datetime(rate_new['掛牌日期'], format='%Y/%m/%d')
#print(rate)
print(rate_new)
plt.plot(rate_new.iloc[:,0],rate_new.iloc[:,1])
rate_reverse = rate_new.iloc[:,1][::-1]
x = np.array(range(days))
y = np.array(rate_reverse)
m,k = np.polyfit(x,y,1)
y2=0
deg = int(input('請輸入最小平方法最高次數：（建議不要10次以上）'))
z = np.polyfit(x,y,deg)
#print(z)
for power in range(deg+1):
  y2 = y2 + z[deg-power]*x**(power)
plt.plot(rate_new.iloc[:,0],y2[::-1])
plt.title("jpy to twd") 
plt.ylabel("rate") 
plt.xlabel("time")
t = int(input('請輸入要預估幾天後的匯率：'))
f = 0
for power in range(deg+1):
  f = f + z[deg-power]*(t+days-1)**(power)
print(t,'天後的匯率為：',f)
plt.show()
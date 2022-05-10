import urllib.request
import json
from datetime import datetime, timedelta
from pandas import read_csv

utctime = datetime.utcnow()
bjtime = utctime + timedelta(hours=8)
bjtime = bjtime.strftime('%m-%d')

data = urllib.request.urlopen("https://api.bilibili.com/x/web-interface/card?mid=1947291841")
xinxi = data.read().decode('utf-8')
dict = json.loads(xinxi)
fans = dict['data']['card']['fans']
add_info = bjtime + ',' + str(fans) + '\n'

with open('data.csv','a') as f:
    f.write(add_info)
    



import matplotlib.pyplot as plt

series = read_csv('data.csv',header=0, index_col=0, parse_dates=True, squeeze=True)

series.plot()
plt.xlabel('Date')

plt.savefig('粉丝数趋势.jpg', bbox_inches='tight', dpi=360)
#输出图片并去除白边

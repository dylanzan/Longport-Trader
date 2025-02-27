import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

from longport.openapi import QuoteContext, Config

from __init__ import LONGPORT_API_ACCESS_TOKEN, LONGPORT_API_APP_KEY, LONGPORT_API_APP_SECRET

# import CapitalFlowIntradayResponse_pb2 as CapitalFlowIntradayResponse_pb2

symbol = '3067.HK'

config = Config(app_key=LONGPORT_API_APP_KEY, app_secret=LONGPORT_API_APP_SECRET,
                access_token=LONGPORT_API_ACCESS_TOKEN)

quote_ctx = QuoteContext(config)

resp_list = quote_ctx.capital_flow(symbol)

data_list = [
    {'timestamp': v.timestamp.strftime("%Y-%m-%dT%H:%M:%SZ"), 'inflow': float(v.inflow)}
    for v in resp_list
]

print(data_list)

# 提取时间戳和流入数据
timestamps = [item['timestamp'] for item in data_list]
inflows = [item['inflow'] for item in data_list]

# 创建图形和坐标轴
plt.figure(figsize=(10, 6))

# 绘制折线图
plt.plot(timestamps, inflows, marker='o', color='b', label='Capital Flow')

# 格式化时间轴显示
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))  # 显示小时:分钟
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=5))  # 每5分钟标记一次

# 自动旋转日期标签
plt.xticks(rotation=45)

# 设置标题和标签
plt.title('Capital Flow Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Inflow Amount')

# 添加图例
plt.legend()

# 显示图形
plt.tight_layout()
plt.show()

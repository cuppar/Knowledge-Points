import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

stock_price_range = np.linspace(2, 50, 20, dtype=float)
stock_num_range = np.linspace(1000, 1000000, 20, dtype=float)

stock_price, stock_num = np.meshgrid(stock_price_range, stock_num_range)

YONG_JIN = 0.003  # 佣金=成交额×佣金率 (小于5元按5元算)
GUO_HU = 1000  # 过户费=股数/1000 (小于1元按1元算)
YIN_HUA = 0.001  # 印花税=卖出价的0.001 (只在卖出时收取)


# 买入佣金
tax_buy_yongjin = (YONG_JIN*stock_num*stock_price)
# 买入过户费
tax_buy_guohu = (stock_num/GUO_HU)
# 买入总成本
buy_total = (stock_price*stock_num+tax_buy_yongjin+tax_buy_guohu)
# 卖出保底总价
sell_total_minimum = ((buy_total+tax_buy_guohu)/(1-YONG_JIN-YIN_HUA))
# 每股的上税
tax_p_stock = (sell_total_minimum-buy_total)/(stock_num*stock_price)

'''
tax_p_stock = (((((stock_price*stock_num+(YONG_JIN*stock_num*stock_price)
                   + (stock_num/GUO_HU))
                  + (stock_num/GUO_HU))/(1-YONG_JIN-YIN_HUA))
                - (stock_price*stock_num+(YONG_JIN*stock_num*stock_price)
                   + (stock_num/GUO_HU)))/stock_num)
'''

# tax_p_stock = (((stock_price*stock_num*1.003+stock_num/1000.0) + stock_num/1000.0) / (0.996) - (stock_price*stock_num*1.003+stock_num/1000.0))

# 画图
fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(stock_price, stock_num, tax_p_stock)
plt.show()

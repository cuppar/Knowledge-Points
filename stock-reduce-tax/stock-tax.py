import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 买股票的变量： 股价 和 股数
stock_price_range = np.linspace(3.6, 17, 5, dtype=float)
stock_num_range = np.linspace(100, 600, 5, dtype=float)

stock_price, stock_num = np.meshgrid(stock_price_range, stock_num_range)

# 常量 上税的比例
YONG_JIN = 0.003  # 佣金=成交额×佣金率 (小于5元按5元算)
GUO_HU = 1000  # 过户费=股数/1000 (小于1元按1元算)
YIN_HUA = 0.001  # 印花税=卖出价的0.001 (只在卖出时收取)


# 买入佣金
tax_buy_yongjin = (YONG_JIN*stock_num*stock_price)
if tax_buy_yongjin.any() <= 5:
    tax_buy_yongjin = 5
# 买入过户费
if stock_num.any() >= 1000:
    tax_buy_guohu = (stock_num/GUO_HU)
else:
    tax_buy_guohu = 1
# 买入总成本
buy_total = (stock_price*stock_num+tax_buy_yongjin+tax_buy_guohu)
# 卖出保底总价
sell_total_minimum = ((buy_total+tax_buy_guohu)/(1-YONG_JIN-YIN_HUA))

# 每股的上税率=每股上税/股价
tax_p_stock = (sell_total_minimum-buy_total)/stock_num/stock_price

'''
# 每股的上税
tax_p_stock = (sell_total_minimum-buy_total)/(stock_num*stock_price)
'''
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

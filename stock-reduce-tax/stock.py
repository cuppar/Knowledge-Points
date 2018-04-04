#! /usr/bin/python3

# ***** 股票计算器 *****

# 常量 上税的比例
YONG_JIN = 0.003  # 佣金=成交额×佣金率 (小于5元按5元算)
GUO_HU = 1000  # 过户费=股数/1000 (小于1元按1元算)
YIN_HUA = 0.001  # 印花税=卖出价的0.001 (只在卖出时收取)


def line(title):
    print('*'*15, title, '*'*15)


while 1:
    # input
    print()
    line('股票计算器')
    line('作者 cuppar')
    print()
    line('请输入')
    print()
    stock_price = float(input('股价： '))
    stock_num = float(input('数量： '))
    stock_sell_price = float(input('卖价： '))

    # 买入佣金
    tax_buy_yongjin = (YONG_JIN*stock_num*stock_price)
    if tax_buy_yongjin <= 5:
        tax_buy_yongjin = 5
    # 买入过户费
    if stock_num >= 1000:
        tax_buy_guohu = (stock_num/GUO_HU)
    else:
        tax_buy_guohu = 1

    # 买入总成本
    buy_total = (stock_price*stock_num+tax_buy_yongjin+tax_buy_guohu)
    # 卖出保底总价
    sell_total_minimum = ((buy_total+tax_buy_guohu)/(1-YONG_JIN-YIN_HUA))

    # 每股的上税
    tax_p_stock = (sell_total_minimum-stock_num*stock_price)/stock_num

    # 每股的上税率=每股上税/股价
    tax_p_stock_percent = tax_p_stock/stock_price

    # 盈利
    sell_total = stock_sell_price*stock_num*(1-YIN_HUA-YONG_JIN)-tax_buy_guohu
    win = sell_total-buy_total

    # output
    print()
    print('分析如下：')
    line('信息')

    print('股价：', stock_price)
    print('数量:', stock_num)
    print('成交额：', stock_num*stock_price)
    print('买入总上税: %.4f' % (buy_total-stock_num*stock_price))
    print('买入总成本： %.4f' % (buy_total))

    line('保本')

    print('每股涨 {0:.5f} 才能保本。'.format(tax_p_stock))
    print('即股价大于： {0:.5f} 卖出。'.format(stock_price+tax_p_stock))
    print('每股上税率为 {0:.6f} (卖出税率以保本价卖出计算)。'.format(tax_p_stock_percent))

    line('盈利')
    print('卖出收入： {0:.5f} '.format(sell_total))
    print('净利润： {0:.5f} '.format(win))
    line('')
    print()

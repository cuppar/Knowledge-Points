#! /usr/bin/python3

# ***** 股票计算器 *****

# 常量 上税的比例
YONG_JIN = 0.003  # 佣金=成交额×佣金率 (小于5元按5元算)
GUO_HU = 1000  # 过户费=股数/1000 (小于1元按1元算)
YIN_HUA = 0.001  # 印花税=卖出价的0.001 (只在卖出时收取)

# 买入成交额+税=成本 卖出成交额-税=收入 收入-成本=利润


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

    # **买入**
    # *成交额*
    # 买入成交额
    buy_cje = stock_price*stock_num
    # *税*
    # 买入佣金
    tax_buy_yongjin = (YONG_JIN*buy_cje)
    if tax_buy_yongjin <= 5:
        tax_buy_yongjin = 5
    # 买入过户费
    if stock_num >= 1000:
        tax_buy_guohu = (stock_num/GUO_HU)
    else:
        tax_buy_guohu = 1
    # *总额*
    # 买入总成本
    buy_total = buy_cje+tax_buy_yongjin+tax_buy_guohu

    # **保底卖出**
    # *保底卖出成交额*
    # 卖出过户税和买入过户税相同
    tax_sell_guohu_baodi = tax_buy_guohu
    # 卖出成交额(保底)
    sell_cje_baodi = ((buy_total+tax_sell_guohu_baodi)/(1-YONG_JIN-YIN_HUA))
    # *税*
    # 过户费(在*保底卖出成交额*栏目下)
    # 卖出印花税(保底)
    tax_sell_yinhua_baodi = sell_cje_baodi*YIN_HUA
    # 卖出佣金(保底)
    tax_sell_yongjin_baodi = sell_cje_baodi*YONG_JIN
    if tax_sell_yongjin_baodi < 5:
        tax_sell_yongjin_baodi = 5
    # *卖出收入(保底)* 等于支出总成本

    # **真实卖出**
    # *成交额*
    # 卖出成交额
    sell_cje = stock_sell_price*stock_num
    # *税*
    # 过户费
    tax_sell_guohu = tax_buy_guohu
    # 印花税
    tax_sell_yinhua = sell_cje*YIN_HUA
    # 佣金
    tax_sell_yongjin = sell_cje*YONG_JIN
    if tax_sell_yongjin < 5:
        tax_sell_yongjin = 5
    # *卖出收入*
    sell_total = sell_cje-tax_sell_guohu-tax_sell_yinhua-tax_sell_yongjin

    # ***统计值***
    # **保底价卖出**
    # 总税(保底)
    tax_total_baodi = tax_buy_guohu+tax_buy_yongjin+tax_sell_guohu_baodi\
        + tax_sell_yongjin_baodi+tax_sell_yinhua_baodi
    # 每股上税baodi
    tax_p_stock_baodi = tax_total_baodi/stock_num
    # 每股上税率baodi
    tax_p_stock_precent_baodi = tax_p_stock_baodi/stock_price

    # **真实价卖出**
    # 总税
    tax_total = tax_buy_guohu + tax_buy_yongjin + tax_sell_guohu\
        + tax_sell_yongjin + tax_sell_yinhua
    # 每股上税
    tax_p_stock = tax_total/stock_num
    # 每股上税率
    tax_p_stock_precent = tax_p_stock/stock_price
    # 利润
    win = sell_total-buy_total

    # output
    print()
    print('分析如下：')
    line('信息')

    print('股价：', stock_price)
    print('数量:', stock_num)
    print('买入成交额： {0:.6f}'.format(buy_cje))
    print('卖出成交额： {0:.6f}'.format(sell_cje))

    line('税')
    print('保底上税： {0:.6f}'.format(tax_total_baodi))
    print('真实上税： {0:.6f}'.format(tax_total))
    print('保底每股上税： {0:.6f}'.format(tax_p_stock_baodi))
    print('真实每股上税： {0:.6f}'.format(tax_p_stock))
    print('保底每股上税率： {0:.6f}'.format(tax_p_stock_precent_baodi))
    print('真实每股上税率： {0:.6f}'.format(tax_p_stock_precent))

    line('保本')
    print('每股涨： {0:.6f} 才能保本'.format(sell_cje_baodi/stock_num-stock_price))
    print('就是涨到： {0:.6f}'.format(sell_cje_baodi/stock_num))

    line('盈利')
    print('买入成本： {0:.6f}'.format(buy_total))
    print('卖出收入： {0:.6f}'.format(sell_total))
    print('利润： {0:.6f}'.format(win))

    line('')
    print()

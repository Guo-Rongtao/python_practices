# 股票数据
stock_codes = (688251, 688163, 600769, 600936, 603626, 605169, 603607, 600778, 603060, 603728)
stock_names = ('井松智能', '赛伦生物', '祥龙电业', '广西广电', '科森科技', '洪通燃气', '京华激光', '友好集团', '国检集团', '鸣志电器')
stock_prices = (14.91, 14.87, 6.47, 2.16, 6.78, 8.56, 13.94, 5.05, 7.14, 33.55)

# 使用zip函数将元组中的元素逐个配对
stock_info_list = list(zip(stock_codes, stock_names, stock_prices))

# 按照股票代码对股票信息排序
sorted_by_code = sorted(stock_info_list, key=lambda x: x[0])

# 格式化打印按股票代码排序的结果
print("按股票代码排序：")
print("股票代码    股票名称    股票价格")
for code, name, price in sorted_by_code:
    print(f"{code}    {name}    {price}")

# 按照股票价格对股票信息列表排序
sorted_by_price = sorted(stock_info_list, key=lambda x: x[2])

# 格式化打印按股票价格排序的结果
print("\n按股票价格排序：")
print("股票代码    股票名称    股票价格")
for code, name, price in sorted_by_price:
    print(f"{code}    {name}    {price}")

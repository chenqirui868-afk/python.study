funds = [
    {'基金代码': '110022', '基金名称': '易方达消费行业', '净值': 3.2, '份额': 1000},
    {'基金代码': '163402', '基金名称': '兴全趋势投资', '净值': 2.8, '份额': 1500},
    {'基金代码': '519674', '基金名称': '银河创新成长', '净值': 4.5, '份额': 800}
]
for fund in funds:
    print(fund['基金名称'])
for fund in funds:
    net_value = fund['净值']
    quantity = fund['份额']
    market_value = net_value * quantity
    print(f"{fund['基金名称']}的市值:{market_value}")
highest_fund = None
highest_value = 0

for fund in funds:
    market_value = fund['净值'] * fund['份额']
    if market_value > highest_value:
        highest_value = market_value
        highest_fund = fund['基金名称']

print(f"市值最高的基金:{highest_fund}，市值:{highest_value}")


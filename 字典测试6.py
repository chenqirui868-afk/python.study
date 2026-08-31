salesmen = [
    {'姓名': '张三', '销售笔数': 25, '平均客单价': 8000},
    {'姓名': '李四', '销售笔数': 18, '平均客单价': 12000},
    {'姓名': '王五', '销售笔数': 32, '平均客单价': 6000},
    {'姓名': '赵六', '销售笔数': 20, '平均客单价': 10000}
]
for salesman in salesmen:
    sales_count = salesman['销售笔数']
    sales_value = salesman['平均客单价']
    total_sales = sales_count * sales_value
highest_name = None
highest_sales = 0
for salesman in salesmen:
    total_sales = sales_count * sales_value
    if total_sales > highest_sales:
        highest_sales = total_sales
        highest_name = salesman['姓名']
        print(f"总销售额最高的销售员：{highest_name},最高销售额：{highest_sales}")


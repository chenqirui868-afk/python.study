jan_sales = {'产品A': 500, '产品B': 300, '产品C': 200}
feb_sales = {'产品A': 600, '产品B': 350, '产品D': 150}
mar_sales = {'产品A': 550, '产品B': 320, '产品C': 180}
result = jan_sales.copy()
for product, sales in feb_sales.items():
    if product in result:
        result[product] = result[product] + sales
    else:
        result[product] = sales
for product, sales in mar_sales.items():
    if product in result:
        result[product] = result[product] + sales
    else:
        result[product] = sales
print("合并后的数据")
print(result)
highest_product = None
highest_sales = 0
for product,sales in result.items():
    if sales >highest_sales:
        highest_sales = sales
        highest_product = product
    print(f"销售数量最多的产品：{highest_product},销售量：{highest_sales}")
common_products = []
for product in jan_sales:
    if product in feb_sales and mar_sales:
        common_products.append(product)
print(f"三个月都有销售的产品:{common_products}")
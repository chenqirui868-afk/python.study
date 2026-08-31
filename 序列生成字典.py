products = ['手机', '电脑', '平板']
prices = [5000, 8000, 3000]
product_dict = dict(zip(products,prices))
print(product_dict)


products = ['手机', '电脑', '平板']
sales_dict = dict.fromkeys(products,0)
print(sales_dict)

products = ['手机', '电脑', '平板']
prices = [5000, 8000, 3000]
product_dict = {p:pr for p,pr in zip(products,prices)}
print(product_dict)

employees = ['张三', '李四', '王五']
base_salary = [8000, 9000, 7500]
employees_dict = dict(zip(employees,base_salary))
print(employees_dict)

products = ['苹果', '香蕉', '橙子']
products_dict = dict.fromkeys(products,0)
print(products_dict)
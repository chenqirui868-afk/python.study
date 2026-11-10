import pandas as pd

#读取购物车详情数据
df = pd.read_csv('basket_details.csv')

#打印前5行
print(df.head(5))
#question1:找出购买最活跃的前三名顾客
top_customers = df['customer_id'].value_counts().head(3)
print("\n--- Top 3 Active Customers ---")
print(top_customers)
print("Business Conclusion: Customer 11082470 ,8276934 and 18617678 are our most active buyers,we should \
target them with VIP promotions")
#question2:找出最受欢迎的 top 3商品
top_products = df['product_id'].value_counts().head(3)
print("\n--- Top 3 Popualr Products ---")
print(top_products)
print("Business Conclusion: Product 43524799,31516269 and 39833031 are our most popular products,we\
must ensure they never run out of stock")
q1_revenue = {'云服务': 500, '软件产品': 800, '咨询服务': 300}
q2_revenue = {'云服务': 600, '软件产品': 750, '硬件销售': 250}
for product,revenue in q2_revenue.items():
    if product in q1_revenue:
        q1_revenue[product] = revenue+ q1_revenue[product]
    else:
        q1_revenue[product] = revenue 
        print(q1_revenue)
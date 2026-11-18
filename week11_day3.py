import matplotlib.pyplot as plt

products = ['Wine Glass', 'Shaker Cup', 'Running Vest']
sales = [120, 250, 180]

plt.figure(figsize=(15,5))

plt.subplot(131)
plt.bar(products,sales)
plt.title("Sales by Product")

plt.subplot(132)
plt.scatter(products,sales)
plt.title("Sales Distribution")

plt.subplot(133)
plt.plot(products,sales)
plt.title("Sales Trend")

plt.suptitle("Products Sales Analysis")
plt.show()

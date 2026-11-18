import matplotlib.pyplot as plt

advertising = [10, 20, 30, 40, 50, 60, 70, 80]

sales = [200, 180, 220, 170, 160, 140, 130, 100]

plt.scatter(advertising,sales,color='red')
plt.title("Advertising and Sales Analysis")

plt.xlabel("Advertising Spending")
plt.ylabel("Sales Revenue")
plt.grid(True)

plt.show()
import matplotlib.pyplot as plt

advertising = [10, 20, 30, 40, 50, 60, 70, 80]

sales = [100, 120, 150, 160, 190, 210, 240, 270]

plt.scatter(advertising,sales)
plt.title("Advertising vs Sales")

plt.xlabel("Advertising Spending")
plt.ylabel("Sales Revenue")

plt.show()
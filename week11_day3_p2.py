import matplotlib.pyplot as plt

spending = [
    35, 45, 50, 55, 60,
    65, 70, 75, 80, 85,
    90, 95, 100, 110, 120,
    130, 140, 150, 160, 180,
    200, 220, 250, 280, 300
]

plt.hist(spending, bins=5)
plt.title("Customer Spending Distribution")

plt.xlabel("Spending Amount")
plt.ylabel("Frequency")

plt.show()
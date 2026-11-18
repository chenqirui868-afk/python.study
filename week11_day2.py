import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
revenue = [300, 450, 380, 600, 750]

plt.plot(days, revenue, 'ro')


plt.title('Daily Revenue Analysis')
plt.xlabel('Days')
plt.ylabel('Revenue')
plt.axis((0, 6, 0, 800))

plt.grid(True)

plt.show
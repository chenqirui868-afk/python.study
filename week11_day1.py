import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt

plt.title('Monthly Sales')

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
sales = [120, 150, 180, 140, 200]

plt.xlabel('months')
plt.ylabel('sales')

plt.plot(months, sales, marker='o')
plt.tight_layout()
plt.savefig('monthly_sales.png', dpi=150)
print('Chart saved as monthly_sales.png')
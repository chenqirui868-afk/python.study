import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()
tips = sns.load_dataset("tips")
sns.scatterplot(
      data=tips,
      x="total_bill",
      y="tip",
      hue="smoker",
      style="smoker"
      
)
plt.title("Restaurant Tips Analysis")
plt.xlabel("Total Bill")
plt.ylabel("Tip Amount")

plt.show()
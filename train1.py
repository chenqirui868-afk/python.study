prices = [100,102,98,105,99,110,95]
names = ["Apple","Google","Microsoft","Amazon","Tesla","Facebook","Intel"]
for i in range(len(prices)):
    price = prices[i]
    name = names[i]
    if price > 100:
        print(name, "-", price)
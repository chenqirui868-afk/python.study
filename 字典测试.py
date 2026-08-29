stocks = {'60071':11.95,
          '603161':15.66,
          '002436':33.60}
print(stocks["603161"])
price = stocks['002436']
stocks['002436'] = 35.70
stocks['159501'] = 2.103
del stocks['60071']
print(stocks,price)
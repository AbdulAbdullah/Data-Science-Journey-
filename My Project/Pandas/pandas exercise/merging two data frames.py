'''merge two data frames'''
import pandas as pd

Car_Price = {'company': ['Innoson', 'Kia Rio', 'Nissan Almera', 'Peugeot 301'], 'price': [4000000, 5000000, 4000000, 3000000]}

carPriceDf = pd.DataFrame.from_dict(Car_Price)

Car_Horsepower = {'company': ['Innoson', 'Kia Rio', 'Nissan Almera', 'Peugeot 301'], 'horsepower': [560, 300, 1200, 300]}

carHorsepowerDf = pd.DataFrame.from_dict(Car_Horsepower)

carsDf = pd.merge(carPriceDf, carHorsepowerDf, on="company")

print(carsDf)
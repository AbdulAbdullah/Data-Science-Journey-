'''concatenate two data frames using the following conditions '''
import pandas as pd

NigerianCars = {'company': ['Innoson', 'Kia Rio', 'Nissan Almera', 'Peugeot 301'], 'price': [4000000, 5000000, 4000000, 3000000]}

carsDf1 = pd.DataFrame.from_dict(NigerianCars)

GermanCars = {'company': ['Ford', 'mercedes', 'BMW', 'Audi' ], 'price': [5000000, 1000000, 1200000, 3000000]}

carsDf2 = pd.DataFrame.from_dict(GermanCars)

carsDf = pd.concat([carsDf1, carsDf2], keys=["Nigerian", "German"])

print(carsDf)
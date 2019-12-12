'''sort the cars by price column'''
import pandas as pd

df = pd.read_csv('C:\\Users\\ABDUL\\Documents\\My Project\\Pandas\\pandas exercise\\Automobile_data.csv')

#   sort price and horsepower
carsDf = df.sort_values(by=['price', 'horsepower'], ascending=False)

#   print first five
print(carsDf.head(5))

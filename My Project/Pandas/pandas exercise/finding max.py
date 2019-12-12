'''finding the most expensive car company name on the list'''
import pandas as pd

df = pd.read_csv('C:\\Users\\ABDUL\\Documents\\My Project\\Pandas\\pandas exercise\\Automobile_data.csv')

df = df[['company', 'price']][df.price == df['price'].max()]

print(df)

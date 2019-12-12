'''count the total number of cars per company'''
import pandas as pd

df = pd.read_csv('C:\\Users\\ABDUL\\Documents\\My Project\\Pandas\\pandas exercise\\Automobile_data.csv')

print(df['company'].value_counts())


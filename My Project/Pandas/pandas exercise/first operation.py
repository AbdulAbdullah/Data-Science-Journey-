'''from the data given  print the first and last five rows'''
import pandas as pd

df = pd.read_csv('C:\\Users\\ABDUL\\Documents\\My Project\\Pandas\\pandas exercise\\Automobile_data.csv')

'''print the first five rows'''
print(df.head(5))

'''print the last five rows'''
print(df.tail(5))
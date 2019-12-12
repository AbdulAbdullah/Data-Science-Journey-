'''clean the data given and update the file'''
import pandas as pd

df = pd.read_csv('C:\\Users\\ABDUL\\Documents\\My Project\\Pandas\\pandas exercise\\Automobile_data.csv',

#replacing  the columns with ? and n.a to NAN
                 na_values={
                     'price': ["?", "n.a"],
                     'stroke': ["?", "n.a"],
                     'horsepower': ["?", "n.a"],
                     'peak-rpm': ["?", "n.a"],
                     'average-mileage': ["?", "n.a"]})


print(df)

df.to_csv('C:\\Users\\ABDUL\\Documents\\My Project\\Pandas\\pandas exercise\\Automobile_data.csv')


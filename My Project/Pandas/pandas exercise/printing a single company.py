'''print all bmw and porsche cars'''
import pandas as pd

df = pd.read_csv('C:\\Users\\ABDUL\\Documents\\My Project\\Pandas\\pandas exercise\\Automobile_data.csv')

# grouping by company name
car_company = df.groupby('company')

# getting data from porsche company
porscheDF = car_company.get_group('porsche')

# getting data from BMW company
bmwDF = car_company.get_group('bmw')

print(bmwDF, porscheDF)

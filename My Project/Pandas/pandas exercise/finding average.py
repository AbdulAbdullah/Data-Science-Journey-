'''find the average milage of each car making company'''
import pandas as pd

df = pd.read_csv('C:\\Users\\ABDUL\\Documents\\My Project\\Pandas\\pandas exercise\\Automobile_data.csv')

car_companies = df.groupby('company')

mileageDF = car_companies['company', 'average-mileage'].mean()

print(mileageDF)
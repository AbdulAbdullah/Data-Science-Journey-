import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


style.use('fivethirtyeight')


#Reading the file from it's location
country = pd.read_csv('C:\\Users\\ABDUL\\Documents\\My Project\\Pandas\\unemployment rate.csv', index_col=0)


df = country.head(5)

#the index value is country code
df = df.set_index(["Country Code"])

#reading from 2011 to 2012
sd = df.reindex(columns=['2011', '2012'])

#difference between between the two columns
db = sd.diff(axis=1)

db.plot(kind = 'bar')
plt.show()


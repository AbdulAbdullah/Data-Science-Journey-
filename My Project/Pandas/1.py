import pandas as pd

abd_web = {'Day':[1,2,3,4,5,6], "visitors": [1000,700,6000,1000,400,350], 'Bounce_Rate':[20,20,23,15,10,34]}

df = pd.DataFrame(abd_web)
print(df)
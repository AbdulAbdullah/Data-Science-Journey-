import pandas as pd

df1 = pd.DataFrame({"HPI": [80, 90, 50, 60], "Int_rate": [2, 3, 4, 3], "NG_GDP": [40, 30, 70, 65]},
                   index=[2001, 2004, 2014, 20015])

df2 = pd.DataFrame({"Low_Tier_HPI": [50, 40, 67, 34], "Unemployment_rate": [1, 3, 5, 6]},
                   index=[2001, 2004, 2014, 20015])

'''MERGING'''
'''merge  = dp.merge(df1, df2)
print(merge)
'''

'''JOINING'''
joined = df1.join(df2)
print(joined)

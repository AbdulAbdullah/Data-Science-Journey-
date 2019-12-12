import pandas as pd

df1 = pd.DataFrame({"HPI": [80, 90, 50, 60], "Int_rate": [2, 3, 4, 3], "NG_GDP_Thousand": [40, 30, 70, 65]},
                   index=[2001, 2002, 2005, 2007])

df2 = pd.DataFrame({"HPI": [80, 90, 50, 60], "Int_rate": [2, 3, 4, 3], "NG_GDP_Thousand": [40, 30, 70, 65]},
                   index=[2009, 2011, 2013, 20015])

concat = pd.concat([df1, df2])
print(concat)
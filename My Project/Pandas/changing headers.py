import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style


df = pd.DataFrame({"Day": [1, 2, 3, 4], "Visitors": [200, 100, 230, 300], "Bounce_Rate": [20, 45, 60, 10]})
#Changing headers
df = df.rename(columns={"Visitors":"Users"})

print(df)
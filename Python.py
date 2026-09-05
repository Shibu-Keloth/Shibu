import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Math": [40,50,60,70,80],
    "Science":[45,55,89,78,58],
    "English": [89,98,56,74,69,]
}
df=pd.DataFrame(data)
df["Total"]=df.iloc[:,1:4].sum(axis=1)
df["Average"]=df["Total"]/3
print(df)
df.plot(x="Name", y=["Math","Science", "English"], kind="bar")
plt.title("Students Mark Comparison")
plt.show()
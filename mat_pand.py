import pandas  as pd

import matplotlib.pyplot as plt
 
df=pd.read_csv("pandas.csv")

type_count=df['Type1'].value_counts(ascending=True)

plt.barh(type_count.index,type_count.values,color="blue",edgecolor="black")

plt.title("# of Pokemon by Primary Type ")
plt.xlabel("Count")
plt.ylabel("Type")

plt.tight_layout()

plt.show()
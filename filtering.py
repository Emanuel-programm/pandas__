import pandas as pd

df=pd.read_csv("pandas.csv")

### Filtering = keeping the rows that match condition

# tall_poken=df[df["Height"]>2]

# heavy_pokemon=df[df["Weight"]>100]

# legendary_pokemon=df[df["Legendary"]==True]

water_pokemon=df[(df["Type1"]== "Water") | (df["Type2"]=="Type2")]


ff_pokemon=df[(df["Type1"]=="Fire") & (df["Type2"]=="Flying")]

print(ff_pokemon)


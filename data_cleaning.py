import pandas  as pd


### Data cleaning is the process of fixing/removing:
#### incomplete/incorrect, or irrelevant data
###### --75 % of work done with pandas is data cleaning

df=pd.read_csv("pandas.csv")

# 1 drop irrerevant column
# df=df.drop(columns=["Legendary","No"])

# 2 Handle missing data
# df=df.dropna(subset=["Type2"])

# df=df.fillna({"Type2":"None"})


### Fix inconsistent values

# df["Type1"]=df["Type1"].replace({"Grass":"GRASS","Water":"WATER","Fire":"FIRE"})
# print(df.to_string())


### Standarsize text
# df["Name"]=df["Name"].str.lower()
# print(df.to_string())

#### change data type
# df["Legendary"]=df["Legendary"].astype(bool)


### Removing duplicated data

df=df.drop_duplicates()

print(df.to_string())
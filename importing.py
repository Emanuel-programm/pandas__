import pandas as pd

# df=pd.read_json("your_json.json")
df=pd.read_csv("pandas.csv",index_col="Name")

### SELECTING COLUMN ##############
# print(df["Name"].to_string())
# print(df["Weight"].to_string())
# print(df["Height"].to_string())
# print(df[["Name", "Height", "Weight"]].to_string())

##### SELECTION BY ROWS
#print(df.loc["Pikachu"])
# print(df.loc["Charizard":"Blastoise"],["Height","Weight"])
# print(df.iloc[0:11:2,0:3])


pokemon=input("Enter a Pokemon Name ")

try:
    print(df.loc[pokemon])

except KeyError:
    print(f"{pokemon} Does not Exist")


# print(df.to_string())
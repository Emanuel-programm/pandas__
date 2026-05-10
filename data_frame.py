import pandas as pd
## DataFrame is a tabular data structure with rows and colums (2-Dimensional)

data={
 "names":["Happy","Diana","Marry"],
 "ages":[28,21,40]
}

df=pd.DataFrame(data,index=["lady 1","lady 2","lady 3"])

# print(df.loc["lady 3"])
# print(df.iloc[1])

## Add new column
df["relation"]=["Sis","Wf","Moth"]

print(df)

## Adding a new row
new_rows=pd.DataFrame([{
    "names":"Winner",
    "ages":"25",
    "relation":"Sis"
},
{
    "names":"Frida",
    "ages":"25",
    "relation":"Sis+"
}],

index=["lady 4","Lady 5"])

df=pd.concat([df,new_rows])

print(df)

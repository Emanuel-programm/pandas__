################## series  && dataframe
# Serries is Apandas one dimension array that can hold any data type
## it build on top of numpy array   it means panel data
import pandas as pd


# data=[100,102,103,104,200]
# series=pd.Series(data,index=["a","b","c","d","e"])
# # print(series.loc["d"])
# # print(series.iloc[0])
# print(series[series<200])

calories={
    "day 1":1200,
    "day 2":1300,
    "day 3":1400
}

series=pd.Series(calories)

series.loc["day 3"]+=500
print(series.loc["day 3"])
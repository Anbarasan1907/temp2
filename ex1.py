import pandas as pd
import numpy as np
data=pd.read_csv(r"car_price_prediction_with_missing.csv")
print(data)
print("The first 5 datas of the file are given")
print(data.head(5))
print("Info of the data")
print(data.info())
print("Values those are missing in the data set")
mis_data=data.isnull().sum()
print(mis_data)
print("Dimension of the data frame")
print(data.shape)
print("Data type")
print(type(data))


from enum import Flag
from logging import raiseExceptions
import pandas as pd
df =pd.read_csv('data/processed.csv')
print(df.dtypes)
data_Int_Flag=True
for items in df.dtypes:
    if items !='int64':
        data_Int_Flag=False
if not data_Int_Flag:
    raiseExceptions("data not all integer")

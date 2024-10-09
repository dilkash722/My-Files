import pandas as pd
import numpy as np


arr=np.array([1,2,3,4])
print(arr)

sr=pd.Series(arr)
print(sr)

sr=pd.Series([1,2,3,4])

repeat=sr.repeat(5)
print(repeat)

agg=sr.agg([max,min,sum])
print(agg)

sr1=pd.Series([1,2,3,4,])
sr2=pd.Series([-6,-7,-8,-9])
print(sr1)
print(sr2)
sr3=sr1.append(sr2)
print(sr3)

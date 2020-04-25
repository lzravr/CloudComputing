import pandas as pd
import sys
import numpy as np
import collections, functools, operator 

df = pd.read_csv(sys.argv[1], header=None, dtype={ 0 : str })

listing = df.groupby(0).sum()

print(listing.idxmax()[1])
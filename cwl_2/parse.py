import pandas as pd
import sys
import numpy as np
# from io import StringIO
import uuid

sms = float(sys.argv[2])
poziv = float(sys.argv[3])

df = pd.read_csv(sys.argv[1], header=None, dtype={ 0 : str })

df[1] = df[1].str.strip()
df[1] = df[1].map({'poziv' : poziv, 'sms' : sms})
listing = pd.DataFrame()
listing[0] = df[0]
listing[1] = df[1] * df[2]

listing = listing.groupby(0).sum()

# output = StringIO()
listing.to_csv(str(uuid.uuid1()) + ".csv", header=False)
# print(output.getvalue())
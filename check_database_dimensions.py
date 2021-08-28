import csv
import time
import pandas as pd

df = pd.read_csv("cleaned_doubled_maindatabase.csv")

print(len(df))
print(len(df.columns))

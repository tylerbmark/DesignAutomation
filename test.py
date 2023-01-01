import pandas as pd
from itertools import chain
import os
import argparse
datafile='data.xlsx'
df=pd.ExcelFile(datafile)
# df.sheet_names
sheet_names=', '.join(df.sheet_names)
parser=argparse.ArgumentParser(description=F'Choose: {sheet_names}')
parser.add_argument('--field',type=str,required=True)
args=parser.parse_args()
filename=args.field
print(filename)
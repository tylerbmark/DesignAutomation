import pandas as pd
from itertools import chain
import os
import argparse
datafile='data.xlsx'
filename='Scripts/'

df=pd.ExcelFile(datafile)
sheet_names=df.sheet_names

def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct
def data_to_dict(df_dict_i):
    return Convert(list(chain.from_iterable(df_dict_i['data'])))
for sheet_name in sheet_names:
    df= pd.read_excel(datafile, sheet_name=sheet_name)
    df_dict_i=df.to_dict(orient='split')
    data_dict=data_to_dict(df_dict_i)
    for root, dirs, files in os.walk(filename+sheet_name+'/'+'variable_scripts/'):
        for file in files:
            abs_path=os.path.join(root, file)
            fin=open(abs_path,"rt")
            data=fin.read()
            for i in list(data_dict.keys()):
                data=data.replace('$'+i,str(data_dict[i]))
            fin.close()
            fname,ext=file.split('.')
            new_name=filename+sheet_name+'/'+'new_scripts/'+fname+'_temp'+'.'+ext
            fin=open(new_name,"wt")
            fin.write(data)
            fin.close()
 


import pandas as pd
from itertools import chain
import os
# import argparse
# parser=argparse.ArgumentParser(description='Update the variables')
# parser.add_argument('--file',type=str,required=True)
# args=parser.parse_args()
# filename=args.file
df= pd.read_excel('data.xlsx')
df_dict=df.to_dict(orient='split')
def Convert(a):
    it = iter(a)
    res_dct = dict(zip(it, it))
    return res_dct
def data_to_dict():
    return Convert(list(chain.from_iterable(df_dict['data'])))
data_dict=data_to_dict()
filename='Scripts/'
for root, dirs, files in os.walk(filename+'variable_scripts'):
    for file in files:
        abs_path=os.path.join(root, file)
        fin=open(abs_path,"rt")
        data=fin.read()
        for i in list(data_dict.keys()):
            data=data.replace('$'+i,str(data_dict[i]))
        fin.close()
        fname,ext=file.split('.')
        new_name=filename+'new_scripts/'+fname+'_temp'+'.'+ext
        fin=open(new_name,"wt")
        fin.write(data)
        fin.close()
 


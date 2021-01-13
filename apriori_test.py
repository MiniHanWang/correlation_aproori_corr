# -*- coding: utf-8 -*-
#@Time:2021/1/12 9:52
#@Author: Mini(Wang Han)
#@Site:

from __future__ import print_function
import pandas as pd
def read_data(path):
    if "xls"  in path:
        df_ = pd.read_excel(path)
    elif "csv" in path:
        df_ = pd.read_csv(path)
    else:
        print("the file must be csv or xls or xlsx!")



    return df_
data=read_data(r"600276_恒瑞医药_result.xlsx")
data_x=data.iloc[:,2:4]
#print(data_x)
from apriori import *
support=0.1
confidence=0.5
apriori_result=find_rule(data_x,support,confidence,"-->")
print(apriori_result)
corr=data_x.corr()
print("corr:",corr)

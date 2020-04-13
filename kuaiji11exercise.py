import numpy as np 
import pandas as pd 
import os
import sys 


df = pd.read_excel('D:\MyFiles\MyCode\kuaiji11.xlsx')
print(df)

num_list = df['序号'].tolist()

name_list = df['姓名'].tolist()
name = dict(zip(num_list,name_list))
print(name)

xuehao_list = df['学号'].tolist()
xuehao_list1 = [str(i) for i in xuehao_list]
xuehao = dict(zip(num_list,xuehao_list1))
print(xuehao)


i = 1
for j in range(25):       
    target = xuehao[i] + '-' + name[i]
    os.mkdir(target)
    i = i + 1

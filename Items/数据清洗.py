from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

item_data = pd.read_csv(open('E://Anaconda-code//数据分析数据集.csv'), encoding='utf-8')
list1 = []
list2 = []
list3 = []
list4 = []
data = item_data['Work']
for i in range(len(item_data['Work'])):
    datas = str(data[i])
    Data = datas.split('_')
    list1.append(Data[0].rstrip('薪'))                #删除Salary列中的汉字'薪'
    list2.append(Data[1])
    list3.append(Data[2])
    list4.append(Data[3])


item_data['Salary'] = list1                           #将原始数据中的Work列数据进行清洗
item_data['Address'] = list2                          #将其分割为三列新数据，并将这四列数
item_data['Educated'] = list3                         #据添加到原始数据中，同时删除原始的
item_data['Workexperience'] = list4                   #Work列数据，
item_data.to_csv('清洗后数据集.csv', encoding="utf_8_sig")
print(item_data)
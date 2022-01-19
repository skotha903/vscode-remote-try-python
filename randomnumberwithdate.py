# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 21:52:40 2022

@author: Admin
"""

import datetime
import random
import pandas as pd
import matplotlib.pyplot as plt  
start_date = datetime.date(2019, 10, 31)
my_dict = {"Date":[],"Random Data":[]};
delta = datetime.timedelta(days=1)

while start_date <= datetime.date.today():
    my_dict["Date"].append(start_date)
    start_date += delta
    my_dict["Random Data"].append(str(random.randint(100000,999999)))   
    dataframe = pd.DataFrame(my_dict) 
    dataframe.to_csv('file.csv',index=False)
    dataframe.plot(kind='line',x='Date',y='Random Data')
    plt.show()
    
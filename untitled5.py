# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 10:46:14 2022

@author: Admin
"""
import csv
import numpy
import datetime
from datetime import date
import random
import sys
start = datetime.strftime("31-10-2019", "%d-%m-%Y")
today=date.today()
end=today.strftime("%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
all_list = []
a_list = [] 
f = open('random_num.csv', 'w')
or date in date_generated:
    all_list = []       
    a_list.append(date.strftime("%d-%m-%Y"))
    a_list.append(str(random.randint(100000,999999)))
            
for item in a:
    for i in range(len(item)):
        if i == 0:
            f.write(str(item[i]))
        else:
            f.write(',' + str(item[i]))
    f.write('\n')
f.close()
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 16 16:03:42 2022

@author: Admin
"""

#!/usr/bin/env python3
import datetime
import time
import random
import sys
start = datetime.datetime.strptime("31-10-2019", "%d-%m-%Y")
end = datetime.datetime.strptime("17-01-2022","%d-%m-%Y")
date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
all_list = []
a_list = [] 
columns = 2
rows = 365

for date in date_generated:
    all_list = []
    a_list.append('\n')        
    a_list.append(date.strftime("%d-%m-%Y"))
    a_list.append(str(random.randint(100000,999999)))
    a_list.append('\n')        
    values = ",".join(str(i) for i in a_list)
    print(values)
    all_list.append(a_list)
    print (date.strftime("%d-%m-%Y"))
    sys.stdout = open('random_num.csv', 'w')                  
    for a_list in all_list:
        print (", ".join(map(str, a_list)))
       
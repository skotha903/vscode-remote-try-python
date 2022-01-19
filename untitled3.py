# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 20:05:02 2022

@author: Admin
"""
import csv
import random
import numpy
filename = "Sarada2.CSV"
row_list = [["Date", "Case Numbers"]]
for i in range (1,365):
   month = 1
   year=2021     
   z=i
        
   value=random.randint(1000,10000)
   date=str(z)+"/"+str(month)+"/"+str(year)
   row_list2=[[date,value]]
   array=[] 
   array.append(1)
   a = numpy.array([row_list2])
   with open(filename, 'w', encoding='UTF8') as f:
    writer=csv.writer(f)
    writer.writerows(a)

       

   
   
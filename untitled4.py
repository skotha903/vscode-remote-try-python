# -*- coding: utf-8 -*-
import random
import sys

all_list = []
columns = 2
rows = 365
for x in range(rows):
    if (x<31) is True:
      a_list = []      
      z=x+1
      month="1"
      year="2021"                                        
      date=str(z)+"/"+str(month)+"/"+str(year)                                     
      a_list.append(date)
      a_list.append(str(random.randint(100000,999999)))
        
      values = ",".join(str(i) for i in a_list)
      print (values)        
      all_list.append(a_list)
      z=0
    elif(x>31 and x<60):
        a_list = [] 
        z=z+1
        month="2"
        year="2021"                                        
        date=str(z)+"/"+str(month)+"/"+str(year) 
        a_list.append(date)
        a_list.append(str(random.randint(100000,999999)))
        values = ",".join(str(i) for i in a_list)
        print (values)
        z2=0
    elif(x>59 and x<91):
         a_list = [] 
         z2=z2+1
         month="3"
         year="2021"                                        
         date=str(z2)+"/"+str(month)+"/"+str(year) 
         a_list.append(date)
         a_list.append(str(random.randint(100000,999999)))
         values = ",".join(str(i) for i in a_list)
         print (values) 
         all_list.append(a_list)
         z3=0
    elif(x>90 and x<121):
          a_list = [] 
          z3=z3+1
          month="4"
          year="2021"                                        
          date=str(z3)+"/"+str(month)+"/"+str(year) 
          a_list.append(date)
          a_list.append(str(random.randint(100000,999999)))
          values = ",".join(str(i) for i in a_list)
          print (values) 
          all_list.append(a_list)
          z4=0
    elif(x>120 and x<152):
         a_list = [] 
         z4=z4+1
         month="5"
         year="2021"                                        
         date=str(z4)+"/"+str(month)+"/"+str(year) 
         a_list.append(date)
         a_list.append(str(random.randint(100000,999999)))
         values = ",".join(str(i) for i in a_list)
         print (values) 
         all_list.append(a_list)
         z5=0
    elif(x>151 and x<182):
         a_list = [] 
         z5=z5+1
         month="6"
         year="2021"                                        
         date=str(z5)+"/"+str(month)+"/"+str(year) 
         a_list.append(date)
         a_list.append(str(random.randint(100000,999999)))
         values = ",".join(str(i) for i in a_list)
         print (values) 
         all_list.append(a_list)
         z6=0
    elif(x>181 and x<213):
        a_list = [] 
        z6=z6+1
        month="7"
        year="2021"                                        
        date=str(z6)+"/"+str(month)+"/"+str(year) 
        a_list.append(date)
        a_list.append(str(random.randint(100000,999999)))
        values = ",".join(str(i) for i in a_list)
        print (values) 
        all_list.append(a_list)
        z7=0
    elif(x>212 and x<244):
        a_list = [] 
        z7=z7+1
        month="8"
        year="2021"                                        
        date=str(z7)+"/"+str(month)+"/"+str(year) 
        a_list.append(date)
        a_list.append(str(random.randint(100000,999999)))
        values = ",".join(str(i) for i in a_list)
        print (values) 
        all_list.append(a_list)
        z8=0
    elif(x>243 and x<274):
        a_list = [] 
        z8=z8+1
        month="9"
        year="2021"                                        
        date=str(z8)+"/"+str(month)+"/"+str(year) 
        a_list.append(date)
        a_list.append(str(random.randint(100000,999999)))
        values = ",".join(str(i) for i in a_list)
        print (values) 
        all_list.append(a_list)
        z9=0
    elif(x>273 and x<305):
        a_list = [] 
        z9=z9+1
        month="10"
        year="2021"                                        
        date=str(z9)+"/"+str(month)+"/"+str(year) 
        a_list.append(date)
        a_list.append(str(random.randint(100000,999999)))
        values = ",".join(str(i) for i in a_list)
        print (values) 
        all_list.append(a_list)
        z10=0
    elif(x>304 and x<335):
        a_list = [] 
        z10=z10+1
        month="11"
        year="2021"                                        
        date=str(z10)+"/"+str(month)+"/"+str(year) 
        a_list.append(date)
        a_list.append(str(random.randint(100000,999999)))
        values = ",".join(str(i) for i in a_list)
        print (values) 
        all_list.append(a_list)
        z11=0
    elif(x>334 and x<366):
        a_list = [] 
        z11=z11+1
        month="11"
        year="2021"                                        
        date=str(z10)+"/"+str(month)+"/"+str(year) 
        a_list.append(date)
        a_list.append(str(random.randint(100000,999999)))
        values = ",".join(str(i) for i in a_list)
        print (values) 
        all_list.append(a_list)
sys.stdout = open('random_num.csv', 'w')                  
for a_list in all_list:
    print (", ".join(map(str, a_list)))
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 18:52:39 2022

@author: Admin
"""
import random
import csv
for i in range (1,365):
    if (i<32) is True:
       value=random.randint(1000,10000)
       filename = "Sarada2.CSV"
       with open(filename, 'w', encoding='UTF8') as f:
           writer=csv.writer(f)
           writer.writerows(value)
       
    elif(i>31 and i<60):
      value=random.randint(1000,10000)
      filename = "Sarada.CSV"
      writeFile = open(filename, 'w')
      writeFile.write("%d" % (value))
      writeFile.close()
      print("Month Feburary:")
      print(value)
    elif(i>59 and i<91):  
     value=random.randint(1000,10000)
     filename = "Sarada.CSV"
     writeFile = open(filename, 'w')
     writeFile.write("%d" % (value))
     writeFile.close()
     print("Month March:")
     print(value)
    elif(i>90 and i<121):  
      value=random.randint(1000,10000)
      filename = "Sarada.CSV"
      writeFile = open(filename, 'w')
      writeFile.write("%d" % (value))
      writeFile.close()
      print("Month April:")
      print(value)
    elif(i>120 and i<152):  
      value=random.randint(1000,10000)
      filename = "Sarada.CSV"
      writeFile = open(filename, 'w')
      writeFile.write("%d" % (value))
      writeFile.close()
      print("Month May:")
      print(value)
    elif(i>151 and i<182):  
     value=random.randint(1000,10000)
     filename = "Sarada.CSV"
     writeFile = open(filename, 'w')
     writeFile.write("%d" % (value))
     writeFile.close()
     print("Month June:")
     print(value) 
    elif(i>181 and i<213):  
     value=random.randint(1000,10000)
     filename = "Sarada.CSV"
     writeFile = open(filename, 'w')
     writeFile.write("%d" % (value))
     writeFile.close()
     print("Month July:")
     print(value)        
    elif(i>212 and i<244):  
     value=random.randint(1000,10000)
     filename = "Sarada.CSV"
     writeFile = open(filename, 'w')
     writeFile.write("%d" % (value))
     writeFile.close()
     print("Month August:")
     print(value)         
    elif(i>243 and i<274):  
     value=random.randint(1000,10000)
     filename = "Sarada.CSV"
     writeFile = open(filename, 'w')
     writeFile.write("%d" % (value))
     writeFile.close()
     print("Month September:")
     print(value)
    elif(i>273 and i<305):  
     value=random.randint(1000,10000)
     filename = "Sarada.CSV"
     writeFile = open(filename, 'w')
     writeFile.write("%d" % (value))
     writeFile.close()
     print("Month October:")
     print(value)
    elif(i>305 and i<334):  
      value=random.randint(1000,10000)
      filename = "Sarada.CSV"
      writeFile = open(filename, 'w')
      writeFile.write("%d" % (value))
      writeFile.close()
      print("Month November:")
      print(value)
    elif(i>335 and i<366):  
      value=random.randint(1000,10000)
      filename = "Sarada.CSV"
      writeFile = open(filename, 'w')
      writeFile.write("%d" % (value))
      writeFile.close()
      print("Month December:")
      print(value)
            
            
            
     
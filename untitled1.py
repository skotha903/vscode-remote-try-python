# -*- coding: utf-8 -*-
num = 19
for x in range(1,20):   
   filename = "Sarada %d.csv" %x
   writeFile = open(filename, 'w')
   writeFile.write("%d" % (num))
   writeFile.close()

# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 14:34:06 2022

@author: Admin
"""

import pandas as pd  
name = ["sonu", "monu"] 
subjects= ["Maths", "English"]
marks = [45, 65,] 
dictionary = {'name': name, 'subjects': subjects, 'marks': marks}  
dataframe = pd.DataFrame(dictionary) 
dataframe.to_csv('foo.csv')
# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1sCSPBN7-m6gHc2eaGSUmMoOgi6JeifLR
"""

import pandas as pd
baza={
   "FISH" :["Bahromjonova Marjona","Bahromjonova Mohinabonu","Bahromjonov Kamronbek","Bahromjonov Ixtiyor","Bahromov Umidjon","Bahromov Omadjon",],
   "Manzili":["Farg'ona shahri","Dang'ara tumani","Abdusamad qishlog'i","Abdusamad qishlog'i","Abdusamad qishlog'i","Abdusamad qishlog'i",],
   "Yoshi":["19","16","14","11","8","5",],
   "Ish joyi":["Talaba","o'quvchi","o'quvchi","o'quvchi","o'quvchi","o'quvchi",],
   "Jinsi":["ayol","ayol","erkak","erkak","erkak","erkak",],

}
db=pd.DataFrame(baza)
print(db)

filtr=db[db['Jinsi']=="ayol"]
print(filtr)

filtr1=db[db["Ish joyi"]=="Talaba"]
print(filtr1)
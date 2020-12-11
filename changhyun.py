#!/usr/bin/env python
# coding: utf-8

# In[122]:


import pandas as pd
import numpy as np

data = pd.read_csv("vgsales.csv")

data


# In[182]:


import matplotlib.pyplot as plt

df= data.head(500)
print("here")
# df.groupby(['Genre' , "Platform"]).get_group(["Sports","Wii"])
genre_dic = {}

for genre in df.groupby(['Genre' , "Platform"]):
    try:
        genre_dic[genre[0][0]]
    except Exception as ex:
        genre_dic[genre[0][0]] = {}

for key in genre_dic.keys():
    print(key)
    fig = df.groupby(['Genre' , "Platform"]).size()[key].plot.bar().get_figure()
    fig.savefig("C:\Users\ckmg\OneDrive\바탕 화면\figure\"+key+".png")

# for genre_key in genre_dic.keys():
#     for key in genre_dic[genre_key].keys():
#         print(genre_key + " " + key + " " + str(genre_dic[genre_key][key]))

# for key in dic.keys():
#     print(key + " " + str(dic[key]))
    


# In[161]:


dff.plot(kind='bar')
plt.show()


# In[ ]:





# In[ ]:





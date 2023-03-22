#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import csv


# In[ ]:





# In[63]:


data=pd.read_csv("C:\\Users\\Sathya Sai\\Downloads\\Placement_Data_Full_Class.csv")
data.set_index("sl_no")


# In[52]:


#searching for the missing data
data.isna().sum()


# In[85]:


f=data.groupby('status').sum()
f


# In[64]:


#avereage salary
data[data["status"]=="Placed"]["salary"].mean()


# In[65]:


#finding correlation among the attributes
visual=data.iloc[:,1:]
sns.heatmap(visual.corr(),annot=True)


# In[72]:


temp=data[data["status"]=="Placed"]["mba_p"].min()


# In[73]:


temp


# In[78]:


mba_notplaced=data[data["status"]=="Not Placed"]["mba_p"].max()


# In[77]:


mba_notplaced


# In[148]:


data[data["status"]=="Placed"]


# In[114]:


print("STUDENTS WHO ARE PLACED AND THIER SSC DEGREES")
print(data[data["status"]=="Placed"]["ssc_b"].value_counts())
print("\n\nSTUDENTS WHO ARE NOT PLACED AND THIER SSC DEGREES")
print(data[data["status"]=="Not Placed"]["ssc_b"].value_counts())


# In[102]:


plt.hist(data["ssc_p"],rwidth=0.95)


# In[133]:


print("STUDENTS WHO ARE PLACED AND THIER DEGREES")
print(data[data["status"]=="Placed"]["degree_t"].value_counts())
print("\n\nSTUDENTS WHO ARE NOT PLACED AND THIER  DEGREES")
print(data[data["status"]=="Not Placed"]["degree_t"].value_counts())


# In[134]:


plt.hist(data["degree_p"],rwidth=0.96)


# In[135]:


print("STUDENTS WHO ARE PLACED AND THIER HSC DEGREES")
print(data[data["status"]=="Placed"]["hsc_b"].value_counts())
print("\n\nSTUDENTS WHO ARE NOT PLACED AND THIER HSC DEGREES")
print(data[data["status"]=="Not Placed"]["hsc_b"].value_counts())


# In[136]:


plt.hist(data["hsc_p"],rwidth=0.98)


# In[223]:


print(data[data["status"]=="Placed"]["degree_t"].value_counts())
plt.bar(["Comm&Mgmt","Sci&Tech","Others" ],data[data["status"]=="Placed"]["degree_t"].value_counts())
plt.title("VISUALIZATION OF THE EFFECT OF DEGREE ON PLACEMENT ")
#OBSERVATION-->COMM&MGMT HAS HIGHER IMPORTANCE


# In[167]:


#deg_t=data["degree_t"].unique()
print(data[data["status"]=="Not Placed"]["degree_t"].value_counts())
plt.bar(["Comm&Mgmt","Sci&Tech","Others" ],data[data["status"]=="Not Placed"]["degree_t"].value_counts())


# In[222]:


print(data[data["status"]=="Placed"]["specialisation"].value_counts())
plt.bar(["Mkt&Fin","Mkt&HR"],data[data["status"]=="Placed"]["specialisation"].value_counts())
plt.title("VISUALIZATION OF THE EFFECT OF SPECIALIZATION ON PLACEMENT ")
#OBSERVATION-->Mkt&Fin SPECIALIZATION IS VERY HELPFUL IN PLACEMENTS.


# In[174]:


print(data[data["status"]=="Not Placed"]["specialisation"].value_counts())
plt.bar(["Mkt&HR","Mkt&Fin"],data[data["status"]=="Not Placed"]["specialisation"].value_counts())


# In[221]:


cpm,cpf=0,0
for i in data["gender"][data["status"]=="Placed"]:
    if i=="M":
        cpm+=1
    else:
        cpf+=1

        
print(f"NUMBER OF MALES WHO GOT PLACED={cpm}")
print(f"NUMBER OF FEMALES WHO GOT PLACED={cpf}")

plt.pie([cpm,cpf],labels=["M","F"],explode=[0.05,0],autopct='%.2f%%')
plt.title("PIE CHART OF PLACECEMENTS BASED ON GENDER")
plt.show()
#OBSERVATION:MOSTLY MALES ARE GETTING PLACED       


# In[ ]:





# In[218]:


cnpm,cnpf=0,0
for i in data["gender"][data["status"]=="Not Placed"]:
    if i=="M":
        cnpm+=1
    else:
        cnpf+=1

        
print(f"NUMBER OF MALES WHO GOT PLACED={cnpm}")
print(f"NUMBER OF FEMALES WHO GOT PLACED={cnpf}")

plt.pie([cnpm,cnpf],labels=["M","F"],explode=[0.05,0],autopct='%.2f%%')
plt.show()
        


# In[213]:


print("STUDENTS WHO ARE PLACED AND THIER HSC DEGREES")
print(data[data["status"]=="Placed"]["hsc_s"].value_counts())
print("\n\nSTUDENTS WHO ARE NOT PLACED AND THIER HSC DEGREES")
print(data[data["status"]=="Not Placed"]["hsc_s"].value_counts())


# In[232]:


plt.title("PLACEMENT STATISTICS BASED ON THEIR HSC DEGREES")
plt.pie(data[data["status"]=="Placed"]["hsc_s"].value_counts(),labels=["Commerce","Science","Arts"],explode=[0.01,0.01,0.01],autopct='%.2f%%')
plt.show()
#OBSERVATION-->BEST:COMMERCE


# In[234]:


plt.title("VISUALIZING THE ROLE OF HSC DEGREES IN PLACEMENTS")
plt.pie(data[data["status"]=="Not Placed"]["hsc_s"].value_counts(),labels=["Commerce","Science","Arts"],explode=[0.01,0.01,0.01],autopct='%.2f%%')
plt.show()


# In[235]:


data[data["salary"]==data["salary"].max()]
#observation--->max_salary-->Commerce,Comm&Mgmt,Mkt&Fin.


# In[ ]:


data[""]


# In[ ]:





# In[ ]:





# In[ ]:





# def create_dataset(path):
#     dataset=[]
#     with open (path,'r+') as file:
#         lines=file.readlines()
#         
#     header=headers(lines[0])
#     
#     for i in lines[1:]:
#         val=input_data(i)
#         di=append_column_data(header,val)
#         dataset.append(di)
#     
#     return dataset

# def append_column_data(header,data):
#     dict={}
#     for i,j in zip(header,data):
#         dict[i]=j
#     return dict
# 
# def input_data(data):
#     list=[]
#     for i in data.strip().split(','):
#              list.append(i)
#     return list
# 

# def headers(header):
#     return header.strip().split(",")
# #title=headers(lines[0])

# da=create_dataset("C:\\Users\\Sathya Sai\\Downloads\\Placement_Data_Full_Class.csv")

# In[ ]:





# In[ ]:





# In[ ]:





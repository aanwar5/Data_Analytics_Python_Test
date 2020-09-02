#!/usr/bin/env python
# coding: utf-8

# In[14]:


import warnings
warnings.simplefilter(action = "ignore", category = FutureWarning)
import pandas as pd

import csv 
#creating dataframe by calling it Data Frame
df = pd.read_csv('C:\\Users\\Dell\\Documents\\Custom Office Templates\\SG-Melbourne.csv')
df


# In[17]:


#Making it neater
df1 = pd.read_csv('C:\\Users\\Dell\\Documents\\Custom Office Templates\\SG-Melbourne.csv', index_col= 0)
df1


# In[19]:


df2 = pd.read_csv('C:\\Users\\Dell\\Documents\\Custom Office Templates\\SG-Melbourne.csv', index_col= 3)
print(df2)


# In[22]:


df2.head()


# In[23]:


len(df) #total number of records


# In[24]:


SMI = df2["SMART_METER_INSTALLATION_DATE"]
print(SMI)


# In[25]:


#checking the length of SMI Smart Meter Installations 
len(SMI) #whihc are 78720


# In[26]:


print(SMI.values) #None as of now.


# In[27]:


print(SMI.index)


# In[31]:


SMI.values[0] = "Yes"

SMI.values[2] = " Yes"

print(SMI) #replaced 0 and 1 and 2


# In[33]:


SMI.max() #wont function as this is a mixture of string and float. 


# In[34]:


#Finding the value of a specific location 
SMI.iloc[1000] #--> takes out value of poisition 1000. Unfortunately its nan too lol 


# In[41]:


#same as iloc. 
SMI.values[0]


# In[ ]:





# In[45]:


SMI.values[2340]


# In[47]:


SMI.values[1:100] #prints out values from range 1 to 100.


# In[49]:


SMI.iloc[1:4]
SMI.iloc[4:8]


# In[50]:


df


# In[52]:


df.loc[78717] #takes out 7817 from the columns in df. and tells its specifics.


# In[58]:


df1.loc[8922472]


# In[ ]:





# In[59]:


df1


# In[61]:


SMI.sort_values(ascending=False) #prints out in descending order


# In[65]:


df1.dtypes #seeing what type of data is available


# In[66]:


df1.info()


# In[72]:


df.=pd.read_excel('C:\\Users\\Dell\\Documents\\Custom Office Templates\\datafile(1)')


# In[73]:


print(df1.describe()) #displays mean, standard deviation, minimum, inter-quartile and maximum values 


# In[75]:


print(df1.corr()) #corelation computatition


# In[77]:


print("Head", df1.head()) #displays first 8 data heads from the columns side


# In[80]:


print(df1.columns) #prints out all the columns.


# In[85]:


#adding columns to the file from derived data 
df1["New columns"] = df1["HAS_AGREED_TO_SMS"]
print(df1.columns)


# In[86]:


df1.rename(columns = {"New columns" : "Newer column"}) #replaces the title of a certain column


# In[87]:


mean = df1.INFERRED_CELL.mean()
print("Mean of inferred cells: ", mean) #takes out mean for inferred cells


# In[94]:


import statistics


# In[ ]:





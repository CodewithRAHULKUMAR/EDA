#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[19]:


#1.Exploring data and data cleaning
df=pd.read_csv("US Superstore data.csv")
df


# In[20]:


df.head(10)


# In[23]:


df.isnull().sum().sum()


# In[27]:


df.duplicated().sum()


# In[31]:


df.shape


# In[36]:


df.columns.values


# In[37]:


df["Segment"].value_counts()


# #2 Visualization-Univariate analysis

# In[68]:


plt.figure(figsize=(4,3))
gb=df.groupby("Region").agg({"Region":"count"})
plt.pie(gb['Region'],labels=gb.index,autopct="%1.2f%%")
plt.title("Orders per Region")
plt.show()


# In[71]:


gb=df.groupby("Category").agg({"Category":"count"})
plt.pie(gb["Category"],labels=gb.index,autopct="%0.2ff%%")
plt.legend(loc=2)
plt.show()


# Bivariate Analysis

# In[59]:


df.columns.values


# In[67]:


plt.figure(figsize=(5,4))
cat=sns.countplot(x="Category",data=df,hue="Region")
cat.bar_label(cat.containers[0])
cat.bar_label(cat.containers[1])
cat.bar_label(cat.containers[2])
cat.bar_label(cat.containers[3])
plt.title("Customers per Category")
plt.show()


# In[76]:


#Based on order date
df.info()


# In[78]:


df['Order Date']=df['Order Date'].astype("datetime64[ns]")
df['Ship Date']=df['Ship Date'].astype("datetime64[ns]")


# In[94]:


df['order_year']=df['Order Date'].dt.year


# In[95]:


df.info()


# In[98]:


oy=sns.countplot(x="order_year",data=df)
oy.bar_label(oy.containers[0])
plt.show()


# In[101]:


sns.barplot(x="Category",y="Profit",data=df,estimator='sum')
plt.show() # the black lines represnt variability(bigger the line lesser is its profit)


# In[ ]:





# In[ ]:





# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
import pandas as pd

days = pd.Series(['Monday','Tuesday','Wednesday'])
print(days)


# In[4]:


days_list = np.array(['Monday','Tuesday','Wednesday'])
numpy_days = pd.Series(days_list)
print(numpy_days)


# In[5]:


days = pd.Series(['Monday','Tuesday','Wednesday'], index=['a','b','c'])
print(days)


# In[6]:


days1 = pd.Series({'a':'Monday','b':'Tuesday','c':'Wednesday'})
print(days1)


# In[7]:


days[0]


# In[8]:


days[1:]


# In[9]:


days['c']


# In[10]:


print(pd.DataFrame())


# In[14]:


df_dict = {
    'Country': ['Ghana','Kenya','Nigeria','Togo'],
    'Capital': ['Accra','Nairobi','Abuja','Lome'],
    'Population': [10000, 8500, 35000, 12000],
    'Age': [60, 70, 80, 75]
}

df = pd.DataFrame(df_dict, index=[2,4,6,8])

df_list = [['Ghana','Accra',10000,60],
        ['Kenya','Nairobi',8500,70],
        ['Nigeria','Abuja',35000,80],
        ['Togo','Lome',12000,75]
       ]
df1 = pd.DataFrame(df_list, columns=['Country','Capital','Population','Áge'], index=[2,4,6,8])


# In[16]:


print(df)
print('===============================')
print(df1)


# In[17]:


df.iloc[3]


# In[18]:


df.loc[6]


# In[19]:


df['Capital']


# In[20]:


df.at[6, 'Country']


# In[21]:


df.iat[2,0]


# In[25]:


df.Population.sum()


# In[26]:


df.mean()


# In[27]:


df.describe()


# In[31]:


df_dict2 ={
    'Name': ['James','Yemen','Caro',np.nan],
    'Profession': ['Researcher','Artist','Doctor','Writer'],
    'Experience': [12, np.nan, 10, 8],
    'Height': [np.nan, 175, 180, 150]
}

new_df = pd.DataFrame(df_dict2)
print(new_df)


# In[32]:


new_df.isnull()


# In[33]:


new_df.dropna()


# In[35]:


new_df.fillna(0)


# In[11]:


url = 'https://github.com/WalePhenomenon/climate_change/blob/master/fuel_ferc1.csv?raw=true'
fuel_data = pd.read_csv(url, error_bad_lines=False)
fuel_data.describe(include='all')


# In[22]:


fuel_data.isnull().sum()
fuel_data.count()


# In[38]:


fuel_data.groupby('fuel_unit')['fuel_unit'].count()


# In[41]:


fuel_data[['fuel_unit']] = fuel_data[['fuel_unit']].fillna(value='mcf')
fuel_data.isnull().sum()


# In[42]:


fuel_data.groupby('report_year')['report_year'].count()


# In[48]:


fuel_df1 = fuel_data.iloc[0:19000].reset_index(drop=True)
fuel_df2 = fuel_data.iloc[19000:].reset_index(drop=True)

#check that the length of both dataframes sum to the expected length

assert len(fuel_data) == (len(fuel_df1) + len(fuel_df2))

pd.merge(fuel_df1, fuel_df2, how="inner")


# In[49]:


pd.merge(fuel_df1, fuel_df2, how="outer")


# In[50]:


pd.merge(fuel_df1, fuel_df2, how="left")


# In[51]:


fuel_data.duplicated().any()


# In[53]:


# Import plotting library

import matplotlib.pyplot as plt
import seaborn as sns


plt.figure(figsize=(7,4))

plt.xticks(rotation=90)

fuel_unit = pd.DataFrame({'unit':['BBL', 'GAL', 'GRAMSU', 'KGU', 'MCF', 'MMBTU', 'MWDTH', 'MWHTH', 'TON'],

            'count':[7998, 84, 464, 110, 11354, 180, 95, 100, 8958]})

sns.barplot(data=fuel_unit, x='unit', y='count')

plt.xlabel('Fuel Unit')



#Because of the extreme range of the values for the fuel unit, we can plot the barchart by taking the logarithm of the y-axis as follows:





g = sns.barplot(data=fuel_unit, x='unit', y='count')

g.set_yscale("log")

g.set_ylim(1, 12000)

plt.xlabel('Fuel Unit')


# In[55]:


sample_df = fuel_data.sample(n=50, random_state=4)
sns.regplot(x=sample_df["utility_id_ferc1"], y=sample_df["fuel_cost_per_mmbtu"], fit_reg=False)


# In[57]:


# Box plot

sns.boxplot(x="fuel_type_code_pudl", y="utility_id_ferc1",

            palette=["m", "g"], data=fuel_data)

# KDE plot 

sns.kdeplot(sample_df['fuel_cost_per_unit_burned'], shade=True, color="b")


# In[4]:


A = [1,2,3,4,5,6] 
B = [13, 21, 34]
A.append(B)
print(A)


# In[24]:


fuel_data.kurt(axis=0)


# In[13]:


fuel_data.skew()


# In[25]:


fuel_data.corr()


# In[ ]:





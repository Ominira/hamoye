#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np

arr = [6,7,8,9]

print(type(arr))


# In[3]:


a = np.array(arr)
print(type(a))
print(a.shape)
print(a.dtype)


# In[4]:


print(a.ndim)


# In[5]:


b = np.array([[1,2,3],[4,5,6]])
print (b)


# In[6]:


print(b.ndim)
b.shape


# In[7]:


# a 2x3 array with random values
np.random.random((2,3))


# In[8]:


# a 2x3 array of zeros
np.zeros((2,3))


# In[3]:


# a 2x3 array of ones
np.ones((2,3))


# In[7]:


# a 3x3 identity matrix
np.identity(3)


# In[13]:


c = np.array([[9.0,8.0,7.0],[1.0,2.0,3.0]])
d = np.array([[4.0,5.0,6.0],[9.0,8.0,7.0]])

c + d


# In[14]:


c * d


# In[15]:


5/d


# In[16]:


c ** 2


# In[17]:


a[0]


# In[19]:


print(a[3])
print(b[0,0])
print(b[1,2])
print(c[0,1])


# In[22]:


d[1,0:2]


# In[23]:


e = np.array([[10,11,12],[13,14,15],[16,17,18],[19,20,21]])
e[:3,:2]


# In[24]:


e[[2,0,3,1],[2,1,0,2]]


# In[25]:


e[e>15]


# In[27]:


np.sum((c,d))


# In[29]:


np.min(d)


# In[30]:


np.mean(d)


# In[35]:


np.corrcoef(c,d)


# In[37]:


import pandas as pd


# In[ ]:





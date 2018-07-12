
# coding: utf-8

# In[1]:


import nltk


# In[3]:


messages = [line.rstrip() for line in open('smsspamcollection/SMSSpamCollection')]


# In[4]:


messages[50]


# In[10]:


for mes_no, message in enumerate(messages[:10]):
    print(mes_no, message)
    print('\n')


# In[11]:


import pandas as pd


# In[12]:


messages = pd.read_csv('smsspamcollection/SMSSpamCollection', sep='\t',names=['label','message'])


# In[14]:


messages.head()


# In[15]:


messages.describe()


# In[16]:


messages['length'] = messages['message'].apply(len)


# In[19]:


messages.head()


# In[20]:


import matplotlib.pyplot as plt


# In[21]:


import seaborn as sns


# In[22]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[30]:


messages['length'].plot.hist(bins=550)


# In[31]:


messages['length'].describe()


# In[33]:


messages[messages['length']==910]


# In[34]:


messages.hist(column='length',by='label',bins=60,figsize=(12,4))


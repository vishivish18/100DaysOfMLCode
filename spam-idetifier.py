
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


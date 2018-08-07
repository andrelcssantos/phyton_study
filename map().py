
# coding: utf-8

# In[2]:


def fahrenheit(T):
    return (9/5) * T + 32


# In[3]:


temp = [9,22,40,90,120]


# In[7]:


temp_f = []
for t in temp:
    temp_f += [fahrenheit(t)]


# In[8]:


list(map(fahrenheit, temp))


# In[10]:


list(map(lambda t:(9/5) * t + 32, temp))


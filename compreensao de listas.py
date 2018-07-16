
# coding: utf-8

# In[1]:


#compreensão em listas
x = []
for i in range(0, 10):
    x += [i] 
    #ou
    x.append(i)


# In[6]:


x2 = [i for i in range(0, 10)]


# In[7]:


x2


# In[8]:


x3 = [i*2 + 10 for i in range(0,10)]


# In[9]:


x3


# In[10]:


#criar listas de pares


# In[11]:


x4 = [i for i in range(0, 20) if i % 2 == 0]


# In[12]:


x4


# In[13]:


lista = []
lista = [letter for letter in 'word']


# In[14]:


lista


# In[15]:


#conversão de temperaturas de celsius para fahrenheit


# In[16]:


cel = [0, 10, 15]


# In[17]:


fah = [temp * (9/5) + 32 for temp in cel]


# In[18]:


fah


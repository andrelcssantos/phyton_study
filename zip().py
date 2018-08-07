
# coding: utf-8

# In[3]:


x = [2, 4, 6, 7, 9, 5, 2]
y = [1, 3, 5, 6, 3, 8, 0]


# In[4]:


list(zip(x,y))


# In[5]:


for i in zip(x, y):
    print(max(i))


# In[6]:


a = [1,2,3,4]
b = [1,2]

list(zip(a,b))


# In[7]:


d1 = {'a':1, 'b': 2}
d2 = {'c':1, 'd': 2}

list(zip(d1, d2.values()))


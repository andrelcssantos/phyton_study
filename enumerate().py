
# coding: utf-8

# In[2]:


l = ['a','b','c','d']
for l in l:
    print(l)


# In[3]:


l = ['a','b','c','d']
for l in enumerate(l):
    print(l)


# In[4]:


l = ['a','b','c','d']
for number, item in enumerate(l):
    print(number, ':', item)


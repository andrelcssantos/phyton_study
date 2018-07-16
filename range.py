
# coding: utf-8

# In[1]:


#permite criar listas pré-determinadas
#utiliza 3 parametros - 1º onde começar a criar a sequencia, 2º até onde vai, 3º internalo entre os números (opcional)
# 1 default


# In[2]:


rangee = range(0, 10, 1) 


# In[3]:


list(rangee)


# In[4]:


range2 = range(0, 30, 2)


# In[5]:


list(range2)


# In[6]:


range3 = range(30, 0, -2)


# In[7]:


list(range3)


# In[8]:


for i in range(0, 10):
    print(i)


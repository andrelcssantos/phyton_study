
# coding: utf-8

# In[1]:


class Animal(object):
    def __init__(self):
        print('Animal criado.')
    
    def quemSouEu(self):
        print('Eu sou um animal')
    
    def comer(self):
        print('Comendo...')


# In[2]:


animal1 = Animal()


# In[3]:


animal1.quemSouEu()


# In[4]:


animal1.comer()


# In[6]:


class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Cachorro criado.')
        
    def quemSouEu(self):
        print('Sou um cachorro.')
    
    def latir(self):
        print('Au Au')


# In[7]:


ada = Cachorro()


# In[8]:


ada.quemSouEu()


# In[9]:


ada.latir()


# In[10]:


ada.comer()



# coding: utf-8

# In[1]:


class Sample(object):
    pass


# In[2]:


x = Sample()


# In[3]:


type(x)


# In[22]:


class Dog(object):
    species='mamifero'
    
    def __init__(self, raca):
        self.raca = raca
        
    def latir(self):
        print('AU AU')


# In[23]:


sam = Dog(raca='Sammy')


# In[24]:


sam.raca


# In[25]:


ada = Dog('Samoieda')


# In[26]:


ada.raca


# In[27]:


ada.species


# In[28]:


ada.latir()


# In[29]:


class Circulo(object):
    pi = 3.14
    
    def __init__(self, raio=1):
        self.raio = raio
        
    def area(self):
        return self.raio ** 2 * self.pi
    
    def defRaio(self, raio):
        self.raio = raio
        
    def obtemRaio(self):
        return self.raio


# In[33]:


c = Circulo(2)


# In[34]:


c.raio


# In[35]:


c.defRaio(3)


# In[36]:


c.raio



# coding: utf-8

# In[26]:


class Book(object):
    def __init__(self, titulo, autor, paginas):
        print('Um livro foi criado.')
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    def __str__(self):
        return 'Título {a} do Autor {b}'.format(a=self.titulo,b=self.autor)
    
    def __len__(self):
        return self.paginas
    
    def __del__(self):
        print('Livro destruido')


# In[27]:


sapiens = Book('Sapiens', 'Yuval', 500)


# In[28]:


print(sapiens)


# In[29]:


len(sapiens)


# In[30]:


sapiens.autor


# In[31]:


del sapiens


# In[32]:


print(sapiens)


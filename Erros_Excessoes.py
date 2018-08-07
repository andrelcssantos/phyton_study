
# coding: utf-8

# In[4]:


try:
    file = open('testefile2', 'r')
    file.write('Testando')
except IOError:
    print('Erro ao tratar o arquivo')
else:
    print('Não houve erro')


# In[5]:


try:
    f = open('testfile', 'w')
    f.write('teste novamente')
finally:
    print('Sempre sera executado')



# coding: utf-8

# In[1]:


x = 1
y = 1
while x < 10 and y < 20:
    print('O valor de x * y é: ',x * y)
    x += 1
    y += 2
else:
    print('O valor de x * y é: ',x * y)


# In[2]:


a = 1
lista = []


# In[3]:


lista


# In[4]:


while True:
    lista += [a]
    a += 1
    if a > 10:
        break


# In[5]:


print(lista)


# In[7]:


ate = 50
c = 0
while c < ate:
    c += 1
    if c % 2 == 1:
        continue #retorna para a próxima avaliação
    if c % 2 == 0:
        print(c, 'é par')


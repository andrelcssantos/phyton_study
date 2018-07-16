
# coding: utf-8

# In[2]:


a = 2
b = 3
if a < b:
    print('Falso!!!')


# In[3]:


if b > a:
    print('Verdadeiro!!!')


# In[4]:


if a < b and b == 3:
    print('True!!!!!!!!!')


# In[8]:


c = 2


# In[11]:


bol = a == c


# In[12]:


bol


# In[15]:


if bol:
    print('hehehe')
elif a == b:
    print(':(')


# In[33]:


l = [9, 8, 3]
d = {'Huguinho':9, 'Zezinho':8, 'Luizinho':3}


# In[34]:


i = 2
j = 'Huguinho'
if d[j] >= 9:
    print("Aprovado")
elif d[i] >= 7:
    print("Reprovado")
else: 
    print("Recuperação")


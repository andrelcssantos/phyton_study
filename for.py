
# coding: utf-8

# In[1]:


l = [1,2,3,4,5,6,7,8,9,10]


# In[2]:


for num in l:
    print(num)


# In[4]:


d = {'a':1,'b':2,'c':3,'d':4}


# In[26]:


for x in d.keys():
    print(x)


# In[15]:


for num in l:
    if num % 2 == 0:
        print('Num:',num,' é par!') 
    else: 
        print('Num:',num,' é ímpar!')


# In[16]:


sum_ = 0
for num in l:
    sum_ += num
print(sum_)


# In[17]:


string = 'essa é uma string'
for char in string:
    print(char)


# In[19]:


tup = (1,2,3,4,5)
for t in tup:
    print(t)


# In[20]:


l = [(1,2),(2,3),(3,4)]


# In[21]:


(t1,t2) = l[0]


# In[22]:


for t1 in l:
    print(t1)


# In[23]:


for t2 in l:
    print(t2)


# In[24]:


for (t1,t2) in l:
    print(t1*t2)



# coding: utf-8

# In[15]:


#Implement List Comprehensions
[i for i in 'ACADGLID']
  


# In[17]:


#Implement another list comprehension
[i*n for i in 'xyz' for n in range(1,5)]


# In[22]:


#Implement another list comprehension
[i*n for n in range(1,5) for i in 'xyz']


# In[33]:


#Implement another list comprehension
[[int(i) +n] for n in range(0,3) for i in '234']


# In[118]:


[[i+n for n in range(0,4)]  for i in [2,3,4,5]]


# In[112]:


[(i,n) for i in [1,2,3] for n in [1,2,3]]


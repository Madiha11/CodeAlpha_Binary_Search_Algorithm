#!/usr/bin/env python
# coding: utf-8

# In[8]:


def binary_search_algorithm(range):
    num = 0
    list = []
    while num<=range:
        list.append(num)
        num+=2
    return list
range = int(input())
print(binary_search_algorithm(range))


# In[ ]:





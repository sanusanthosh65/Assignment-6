#!/usr/bin/env python
# coding: utf-8

# #  Assignment 1

# In[7]:


_list1 = [1,2,3,4,5,7,8]
list2 = ['a','b','c','d','e']
dict_1 = {list1[each]:list2[each] 
          for each in range(min(len(list1),len(list2)))}
print(dict_1)


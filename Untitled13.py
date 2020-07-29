#!/usr/bin/env python
# coding: utf-8

# #  Assignment 1

# In[85]:


def merge(list1, list2):   
    merged_list = [] 
    for i in range(max((len(list1), len(list2)))): 
        while True: 
            try: 
                tup = (list1[i], list2[i]) 
            except IndexError: 
                if len(list1) > len(list2): 
                    list2.append('') 
                    tup = (list1[i], list2[i]) 
                continue
            merged_list.append(tup) 
            break
    return merged_list 
  
list1 = [1, 2, 3,4,5,6,7,8] 
list2 =  ["a","b","c","d","e"]

print(merge(list1, list2))


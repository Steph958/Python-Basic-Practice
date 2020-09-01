#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = input("請輸入一個正整數: ")
n = int(n)
for i in range(n):
    if i*i==n:
        print("該數的整數平方根為", i)
        break;
else:
    print("該數並無整數平方根, YOU IDIOT!")
    
    


# In[ ]:


n = int(input("請輸入一個正整數: "))

if n**0.5%1==0:
    print("該數的整數平方根為", n**0.5)
else:
    print("該數並無整數平方根, YOU IDIOT!")


# In[ ]:





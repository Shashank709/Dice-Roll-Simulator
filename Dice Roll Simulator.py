#!/usr/bin/env python
# coding: utf-8

# # Dice Roll Simulator
# 
# The goal is to create a program that will simulate the roll of dice.
# 
# Hint: Using a random module generate a random number between the range from 1 to 6 when the user wants.

# In[1]:


import random

while True:
    print("1. Roll the dice   2. exit")
    user = int(input("enter 1 or 2"))
    if user==1:
        number = random.randint(1,6)
        print("random number generated: ", number)
        
    else:
        break


# In[ ]:





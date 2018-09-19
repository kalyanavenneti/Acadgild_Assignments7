
# coding: utf-8

# In[31]:


# Question 1: Write a function to find moving average in an array over a window:
# Test it over array_input = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of k=3, n=13

# Note: The moving average sequence has n-k+1 elements = 13-3+1= 11 elements

import numpy as np

def moving_avg_arry(array_input, window_size):
    val_array=np.cumsum(array_input,dtype=int)
    val_array[3:]=val_array[3:]-val_array[:-3]
    return val_array[3-1:]/3

x=[3,5,7,2,8,10,11,65,72,81,99,100,150]
array_input=np.array(x)
array_output=moving_avg_arry(array_input,3)

print("Input list:", x)
print("output is:", array_output)


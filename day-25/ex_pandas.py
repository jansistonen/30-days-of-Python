import pandas as pd # importing pandas as pd
import numpy  as np # importing numpy as np

nums = [1,2,3,4,5] # python list
s = pd.Series(nums)
print(s)

#Creating Pandas Series with custom index
s = pd.Series(nums, index=[1,2,3,4,5]) # manually factor the indexed as a parameter
print(s)

fruits = ['bananba', 'mango', 'apple','watermelon','orange']
fruits = pd.Series(fruits, index=[1,2,3,4,5])
print(fruits) # dtype is now object! str = object

#panda series can also med from dictionary
dct = {'name':'Jan', 'country':'Finland','city':'Joensuu','age':31}
s = pd.Series(dct)
print(s)

s = pd.Series(10, index=[1,2,3,4]) #we can make constant, or so to say fill the Series with a given parameter
print(s)

#Creating a Pandas Series Using Linspace

s = pd.Series(np.linspace(5,20,10)) #numpys linspace() 'returns an array of evenly spaced numbers over a specified range.'
print(s)

#DATA FRAMES
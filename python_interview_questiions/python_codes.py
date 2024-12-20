# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RzEy1oebDHVclvTsa5N3wXbh0MrgSvuw

Y=[3,0,2,9],X=[1,5,9,0]return the intersection of the two?it should return 9,0
"""

def intersection(Y,X):
    Y=set(Y)
    X=set(X)

    sets=Y.intersection(X)
    return list(sets)


Y=[3,0,2,9]
X=[1,5,9,0]
res=intersection(Y,X)
print(res)

"""Given an array.find all the duplicates in this array?"""

def duplicate_val(x):
  y=[]
  for i in x:
    if x.count(i)>1:
      if i not in y:
        y.append(i)
  return y
x=[1,2,3,1,3,5,6]
res = duplicate_val(x)
print(res)

"""Rptate a  list to the right by k places,where k is non negative."""

def repeat_list(x,y):
  return x[-y:]+x[:-y]
x=[1,2,3,4,5,6,7]
y=3
res=repeat_list(x,y)
print(res)

"""Givwn an integer array.find the sum of the largest contiguous subarray within the array.if all the elements will be zero it should return 0"""

def sum_of_the_largest_subarray(x):
  max_sum=0
  for i in x:
    if i>0:
      max_sum+=i
  return max_sum


x=[0,0,-3,-4,-1,-2,-1,-5,-4]
res=sum_of_the_largest_subarray(x)
print(res)

"""give an array of strings,group anagrams together"""

def anagrams(x):
  anagram_dict={}
  for i in x:
    sorted_word=''.join(sorted(i))
    if sorted_word in anagram_dict:
      anagram_dict[sorted_word].append(i)
    else:
      anagram_dict[sorted_word]=[i]
  return list(anagram_dict.values())
x=['eat','tea','tan','ate','nat','bat']
res=anagrams(x)
print(res)

"""given a position integer X return an integer that is a factorial of X.I f a negative integer is provided,return -1.implement the soln for recursive function

"""

def recursive_func(x):
  if x<0:
    return -1
  elif x==0:
    return 1
  else:
    return x*recursive_func(x-1)
x=5
res = recursive_func(x)
print(res)

"""given a positive integer X and return an integer that is a factorial of X."""

def fact_value(x):
  if x<0:
    return -1
  elif x==0:
    return 1
  else:
    return x*fact_value(x-1)
x=3
res = fact_value(x)
print(res)


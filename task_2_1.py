# -*- coding: utf-8 -*-
"""task_2.1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rT2GhJ4VqHUGeMLHeEWrGa5TpdK_rRAM
"""

# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
# * [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
# * [42, 54, 65, 87, 0]             -> min = 0, max = 87
# * [5]                             -> min = 5, max = 5
# функции sorted, max и min использовать нельзя!

def maximum(arr):
  max = arr[1]
  for i in arr:
    if i > max:
      max = i
    else:
      continue
  return max
  
def minimum(arr):
  min = arr[1]
  for i in arr:
    if i < min:
      min = i
    else:
      continue
  return min

arr = [-4,-6,-2,-5,1000,63,-134,-566]
minimum(arr)
maximum(arr)
print("max =", maximum(arr), ", min =", minimum(arr))
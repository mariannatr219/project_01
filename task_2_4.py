# -*- coding: utf-8 -*-
"""task_2.4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sOr5TEvbXJ1kWjCTcNRfqfKwKPe1Ajyw

# Задача 2.4.
"""

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"
def remove_exclamation_marks(s):
  b = ""
  for i in range(0, len(s)):
      if s[i] != '!':
        b += s[i]
      else:
        continue
  print(b)
user_answer = input('Введите текст для редактирования ')
remove_exclamation_marks(user_answer)

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"

def remove_last_em(s):
    if s[len(s)-1] == "!":
      a = s[:len(s)-1]
      print(a)
    else:
      print(s)
    
user_answer = input('Введите текст для редактирования ')
remove_last_em(user_answer)
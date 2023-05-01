# -*- coding: utf-8 -*-
"""task_1.2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1opvkgUvqJu5_rNuvmtaWpGl8fdlVfqRJ

#Задача 1.2
"""

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

import random
import datetime

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

k = 3
songs = []
minutes = []
seconds = []
while k != 0:
  random_song = random.choice(my_favorite_songs)
  k -= 1
  songs.append(random_song)
  minute = int(random_song[1])
  second = round(random_song[1] % 1, 2)
  minutes.append(minute)
  seconds.append(second)
total_minute = sum(minutes)
total_seconds = sum(seconds) / 0.60
total_time_m = int(total_minute + total_seconds)
total_time_s = int(total_seconds % 1 *60)


from datetime import time

total_time_new_format = time(minute = int(total_time_m), second = int(total_time_s))


print('Рандомно выбраны 3 трека: ', songs, 'Три песни звучат ', total_time_m, ' минут', total_time_s, 'секунд', total_time_new_format)
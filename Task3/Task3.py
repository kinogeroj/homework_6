# TНапишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

import os
from functools import reduce

os.system('cls')

print('Найдем сумму цифр вещественного числа.')

a = input('Введите вещественное число: ')

l = list(map(int, filter(lambda s: not s.startswith('.'), a)))

print()

print(f'Сумма цифр вещественного числа равна: {reduce(lambda x, y: x + y, l)}')
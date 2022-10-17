# from homework_3
# ================

# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов
# списка, стоящих на нечётной позициях (не индексах).

# num = int(input('Input number: '))
#
#
# def fill_list(n):
#     list = []
#     i = 0
#     while i < n:
#         list.append(random.randint(-10, 10))
#         i += 1
#     print(list)
#     return list
#
#
# def sum_of_odd_elmnts(some_list):
#     i = 0
#     sum = 0
#     while i < len(some_list):
#         sum += some_list[i]
#         i += 2
#     return sum
#
#
# print(f'Sum of elements on odd elements: {sum_of_odd_elmnts(fill_list(num))}')

# ********
# List Comprehensive + Map
# ********

import random

num = int(input('Input number: '))
fill_list = [random.randint(-10, 10) for i in range(num)]
print(fill_list)
print(f'Sum of elements on odd elements: {sum(list(map(int, [fill_list[i] for i in range(0, len(fill_list), 2)])))}')

# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и
# минимальным значением дробной части элементов. минимальное значение дробной части отличное от нуля,
# у целых чисел дробной части нет их в расчет не берем
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import random

num = int(input('Input number: '))


def fill_list(n):
    list = []
    i = 0
    while i < n:
        list.append(round((random.random() * 10), 3))
        i += 1
    print(list)
    return list


def difference(some_list):
    new_list = []
    for i in range(len(some_list)):
        if some_list[i] > 1:
            new_list.append(round((some_list[i] % 1), 3))
        else:
            new_list.append(round((some_list[i]), 3))
    new_list.sort()
    return round((new_list[len(new_list) - 1] - new_list[0]), 3)


print(f'Difference between max & min elements of the list: {difference(fill_list(num))}')

# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д. Если количество нечетное, то центральный # возводим в квадрат и добавляем в конец
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]
import random

num = int(input('Input number: '))


def fill_list(n):
    list = []
    i = 0
    while i < n:
        list.append(random.randint(-10, 10))
        i += 1
    print(list)
    return list


def prod_of_elements(some_list):
    list_of_prod = []
    size = int(len(some_list) / 2)  # длина нового списка
    j = -1  # индекс отсчета с конца листа
    for i in range(size):
        list_of_prod.append(some_list[i] * some_list[j])
        j -= 1
    if len(some_list) % 2 != 0:
        list_of_prod.insert(size, some_list[size] * some_list[size])
    return list_of_prod


print(prod_of_elements(fill_list(num)))

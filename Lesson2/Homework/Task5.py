# Реализуйте алгоритм перемешивания списка.
import random

num = int(input('Input number: '))


def fill_list(n):
    list = []
    for i in range(-n, n + 1):
        list.append(i)
    print(list)
    return list


def shuffle(some_list):
    shuff_list = []
    list_of_indexes = []
    while len(shuff_list) != len(some_list):  # крутим, пока длины массивов не станут равны
        i = int(random.uniform(0, len(some_list)))
        list_of_indexes.append(i)
        exist_count = list_of_indexes.count(i)  # сколько раз наш индекс встречается в списке индексов
        if exist_count < 2:  # если строго 1, то значит такое значение индекса еще не добавляли
            shuff_list.append(some_list[i])
    return shuff_list


print(shuffle(fill_list(num)))

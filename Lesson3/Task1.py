# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.


num = input('Input number to find: ')


def fill_list():
    print('Add some strings to list. Blank line will stop filling the list.')
    list = []
    while True:
        my_string = input()
        if my_string == '':
            break
        else:
            list.append(my_string)
    print(list)
    return list


def find_num_in_list(n, some_list):
    for i in range(len(some_list)):
        if n in some_list[i]:
            print(f'{n} in {i + 1}th element of the list')
        else:
            print('No matches')


find_num_in_list(num, fill_list())

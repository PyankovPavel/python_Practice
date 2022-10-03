# НЕОБЯЗАТЕЛЬНОЕ ЗАДАНИЕ
# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел
import time


# метод наполнения листа цифрами из строки со временем. делаем 1, 2 и 3хзначные числа. Некрасивые 01, 02, 03 и тд меняем
# на 11, 22, 33 и тд


def fill_list():
    s = str(round(time.time() * (13 ** 7)))
    my_list = []
    for i in range(len(s)):
        if i % 2 == 0:
            my_list.append(s[i])
        elif i % 5 == 0:
            my_list.append(s[i] + s[i - 2] + s[i - 1])
        else:
            my_list.append(s[i] + s[i - 1])
    my_list = [i.replace('01', '11') for i in my_list]
    my_list = [i.replace('02', '22') for i in my_list]
    my_list = [i.replace('03', '33') for i in my_list]
    my_list = [i.replace('04', '44') for i in my_list]
    my_list = [i.replace('05', '55') for i in my_list]
    my_list = [i.replace('06', '66') for i in my_list]
    my_list = [i.replace('07', '77') for i in my_list]
    my_list = [i.replace('08', '88') for i in my_list]
    my_list = [i.replace('09', '99') for i in my_list]

    return my_list


# генератор сделал через множество set, он удобен тем, что неупорядочен. отдаем туда пару наших листов, созданных через
# небольшую паузу и забираем необходимое нам кол-во чисел


def generator(n):
    new_list1 = fill_list()
    time.sleep(3)
    new_list2 = fill_list()
    my_set = set(new_list1 + new_list2)
    my_list = list(my_set)
    for i in range(n):
        print(f'({my_list[i]})', end=' ')


num = int(input('How many generated numbers do you want? Please input: '))
print('Ok, wait a sec...', end=' ')
generator(num)

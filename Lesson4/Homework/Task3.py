# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности. Решать через множества и еще каким-нибудь способом кроме множества
# Пример: 47756688399943 -> [5], 1113384455229 -> [8,9], 1115566773322 -> []

num = str(input('Input a number: '))


def find_singles_in_seq(n):
    lst = []
    for i in range(len(num)):
        lst.append(num[i])
    lst.sort()
    print(lst)
    for i in range(len(lst)):
        try:
            if lst[i] != lst[i + 1] and lst[i] != lst[i - 1]:
                print(lst[i], end='  ')
        except:
            if lst[i] != lst[i - 1]:
                print(lst[i])


find_singles_in_seq(num)

# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

num = int(input('Input number: '))


def solution(n):
    list = []
    for i in range(1, n + 1):
        list.append(round((1 + (1 / i)) ** i))
    print(f'List: {list}')
    sum = 0
    for j in range(len(list)):
        sum += list[j]
    return sum


print(f'Sum of elements: {solution(num)}')

# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def is_simple(number):
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


num = int(input('Input number: '))


def solution(n):
    if is_simple(n) and n > 200:
        print(n)
        return

    lst_of_simples = [2, 3, 5, 7]
    for i in range(8, 200):
        if is_simple(i):
            lst_of_simples.append(i)
    result_list = []
    while n > 1:
        for i in range(len(lst_of_simples)):
            if n % lst_of_simples[i] == 0:
                result_list.append(lst_of_simples[i])
                n /= lst_of_simples[i]
                break

    print(result_list)


solution(num)

# 1. Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# *Примеры:*
# - 5, 25 -> да
# - 4, 16 -> да
# - 25, 5 -> да
# - 8,9 -> нет

a = int(input('Input number a '))
b = int(input('Input number b '))


def solution(a, b):
    return a**2 == b or b**2 == a


print(solution(a, b))

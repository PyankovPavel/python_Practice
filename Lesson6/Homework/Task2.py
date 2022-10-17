# from homework_2
# ================
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# def factorial(n):
#     list = []
#     temp = 1
#     for i in range(2, n + 2):
#         list.append(temp)
#         temp *= i
#     return list
#
#
# print(factorial(4))
# print(factorial(6))


# ********
# Map + Lambda
# ********
import math

num = int(input('Input number: '))
print(list(map(lambda i: math.prod(range(1, i + 1)), range(1, num + 1))))

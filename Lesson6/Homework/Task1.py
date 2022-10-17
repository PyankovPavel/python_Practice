# from homework_2
# ================
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример: 6782 -> 23; 0,56 -> 11

# def sumOfNums(n):
#     n = abs(n)
#     if n % 1 != 0:
#         while n % 1 != 0:
#             n *= 10
#             n = round(n, 2)
#
#     sum = 0
#     while n / 10 > 0:
#         sum += n % 10
#         n /= 10
#         n = int(n)
#
#     return sum
#
#
#
# print(sumOfNums(6782))
# print(sumOfNums(0.56))
# print(sumOfNums(198.45))
# print(sumOfNums(0.67))

# ********
# Map
# ********

n = input('Input number: ')
print(sum(list(map(int, n.replace('.', '').replace('', '.').split('.')[1:-1]))))

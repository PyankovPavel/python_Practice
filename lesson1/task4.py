# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3

num = float(input('Введите число: '))

if (num % 1 == 0):
    print('нет')
else:
    print(int(num * 10) % 10)

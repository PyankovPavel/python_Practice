# 3. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

def solution(num):
    if num % 30 == 0:
        return "No"
    elif num % 5 == 0 and num % 10 == 0 or num % 15 != 0:
        return "Yes"
    else:
        return "No"


a = int(input('Input number: '))
print(solution(a))


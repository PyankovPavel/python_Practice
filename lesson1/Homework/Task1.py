# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример: 6 -> да; 7 -> да; 1 -> нет

def func(number):
    if 0 < number < 6:
        print('No, workday')
    elif 5 < number < 8:
        print('Yes, weekend')
    else:
        print('Input number from 1 to 7')


x = int(input('Input number from 1 to 7: '))

func(x)
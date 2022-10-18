# Ввести с клавиатуры 2 числа (int) и вывести в консоль их НОК (наименьшее общее кратное)

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))

max = max(num1, num2)

if max % num1 == 0 and max % num2 == 0:
    print(f'Наименьшее общее кратное для {num1} и  {num2} - {max}')
else:
    for i in range(max, num1*num2+1):
        if i % num1 == 0 and i % num2 == 0:
            print(f'Наименьшее общее кратное для {num1} и  {num2} - {i}')
            break

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Пример: k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0; k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0
import random


def is_null(symbol):
    if symbol == ' + 0' or symbol == '0':
        return True
    else:
        return False


k = int(input('Input value of degree: '))
x = 'x^'
index = 0
list_of_ints = []
for i in range(k + 1):
    list_of_ints.append(random.randint(-15, 15))
list_of_coeffs = [str(s) for s in list_of_ints]
for i in range(len(list_of_coeffs)):
    if i > 0:
        if list_of_coeffs[i].__contains__('-'):
            if list_of_coeffs[i].__contains__('-1'):
                list_of_coeffs[i] = list_of_coeffs[i].replace('-1', ' - ', 1)
            else:
                list_of_coeffs[i] = list_of_coeffs[i].replace('-', ' - ', 1)
        elif list_of_coeffs[i].__contains__('1'):
            list_of_coeffs[i] = list_of_coeffs[i].replace('1', ' + ', 1)
        else:
            list_of_coeffs[i] = list_of_coeffs[i].replace('', ' + ', 1)
    else:
        list_of_coeffs[i] = list_of_coeffs[i].replace('1', '', 1).replace('-1', '', 1)

result = []
while k + 1 > 0:
    if k > 1:
        if not is_null(list_of_coeffs[index]):
            result.append(f'{list_of_coeffs[index]}{x}{k}')
    elif k == 1:
        if not is_null(list_of_coeffs[index]):
            result.append(f'{list_of_coeffs[index]}x')
    else:
        if not is_null(list_of_coeffs[index]):
            result.append(f'{list_of_coeffs[index]}')
    k -= 1
    index += 1
result.append(' = 0')

with open('file.txt', 'w') as file:
    file.write(''.join(result))

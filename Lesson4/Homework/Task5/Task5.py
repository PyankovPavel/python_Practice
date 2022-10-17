# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0
# Результат: # 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

with open('file1.txt', encoding='utf-8') as f1:
    str1 = f1.readline()
with open('file2.txt', encoding='utf-8') as f2:
    str2 = f2.readline()


def str_to_dict(some_str, degree):
    dictionary = {}
    x = some_str[:-3].replace(' ', '').replace('-', ' -').replace('+', ' ').split('x^')
    print(x)
    for i in range(degree):
        x = some_str.find(f'x^{degree}')
        if x != -1:
            y = (some_str[x - 2] + some_str[x - 1])
            dictionary[f'x^{degree}'] = y.strip().replace('+', '1').replace('-', '1')
            degree -= 1
        else:
            degree -= 1
            continue
    return dictionary


def dict_to_str(some_dict: dict):
    list_of_str = []
    for i in range(len(some_dict)):
        list_of_str.append(list(some_dict.values())[i] + list(some_dict.keys())[i])
    result = ' '.join(list_of_str)
    return result


# dict1 = str_to_dict(str1, 9)
# print(dict1)
some_str = '23x^9 - 16x^8 + 3x^7 + 15x^4 - 2x^3 + 1x^2 + 20x^0 = 0'
some_str2 = '17x^9 + 15x^8 - 8x^7 + 15x^6 - 10x^4 + 7x^3 - 13x^1 + 33x^0 = 0'
some_str = some_str[:-3].replace(' ', '').replace('-', ' -').replace('+', ' ').split()
some_str2 = some_str2[:-3].replace(' ', '').replace('-', ' -').replace('+', ' ').split()
print(some_str)
print(some_str2)
for i in range(len(some_str)):
    some_str[i] = some_str[i].split('x^')
    some_str[i] = list(map(int, some_str[i]))
    # if some_str[i][1] !=

for j in range(len(some_str2)):
    some_str2[j] = some_str2[j].split('x^')
    some_str2[j] = list(map(int, some_str2[j]))

print(some_str)
print(some_str2)

# result = []
# for i in range(max(len(some_str), len(some_str2))):
#     first = some_str[i][0]
#     second = some_str2[i][0]
#     if first is not None or second is not None:
#         result[i] = (first if first is not None else 0) + (second if second is not None else 0)
#
# print(result)

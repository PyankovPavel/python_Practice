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


def dict_to_str(some_dict):
    some_dict = dict(some_dict)
    list_of_str = []
    for i in range(len(some_dict)):
        list_of_str.append(list(some_dict.values())[i]+list(some_dict.keys())[i])
    result = ' '.join(list_of_str)
    return result


dict1 = str_to_dict(str1, 9)
dict2 = str_to_dict(str2, 9)
# print(dict1)
# print(dict2)
print(dict_to_str(dict1))

# if list(dict1.keys())[0] == list(dict2.keys())[0]:
#     print(int(list(dict1.values())[0]) + int(list(dict2.values())[0]))
#     dict3[list(dict1.keys())[0]] = int(list(dict1.values())[0]) + int(list(dict2.values())[0])
#
# print(dict3)

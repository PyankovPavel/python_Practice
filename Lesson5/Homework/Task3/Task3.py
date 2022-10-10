# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

with open('input.txt') as inp:
    data_comp = inp.read()

with open('output.txt') as out:
    data_decomp = out.read()


def decompression(some_data):
    words = ''.join(' ' if el.isdigit() else el for el in some_data).split()
    numbers = ''.join(el if el.isdigit() else ' ' for el in some_data).split()
    data_lst = []
    result = ''
    for i in range(len(words)):
        data_lst.append(words[i] * int(numbers[i]))
        result += ''.join(data_lst[i])
    print(result)


def compression(some_data):
    data_lst = []
    for i in range(len(some_data)):
        data_lst.append(some_data[i].lower())
    count_set = set(data_lst)  # оставляем уникальные значения
    count_set = list(count_set)
    count_set.sort()
    result = ''
    for i in range(len(count_set)):
        count = 0
        for j in range(len(data_lst)):
            if count_set[i] == data_lst[j]:
                count += 1
        result += ''.join(f'{count}{count_set[i]}')
    print(result)


compression(data_comp)
decompression(data_decomp)

# 2.	Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

def dictionary(n):
    dict = {}
    n = int(input('Input number: '))
    for i in range(1, n + 1):
        dict[i] = (3 * i) + 1
    return dict


print(dict)

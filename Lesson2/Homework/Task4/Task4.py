# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов
# на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

num = int(input('Input number: '))


def fill_list(n):
    list = []
    for i in range(-n, n + 1):
        list.append(i)
    print(list)
    return list


def prod(some_list):
    open_file = open('file.txt')
    list_of_lines = []
    for line in open_file:
        list_of_lines.append(line.strip())
    open_file.close()
    pos_one = int(list_of_lines[0])
    print(f'pos1 from file.txt is {pos_one}')
    pos_two = int(list_of_lines[1])
    print(f'pos2 from file.txt is {pos_two}')
    print(f'pos1 value ({some_list[pos_one - 1]}) * pos2 value ({some_list[pos_two - 1]}) = ', end='')
    return some_list[pos_one - 1] * some_list[pos_two - 1]


print(prod(fill_list(num)))

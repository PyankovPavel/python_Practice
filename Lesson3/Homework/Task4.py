# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 45 -> 101101; 3 -> 11; 2 -> 10

num = int(input('Input number to convert: '))


def conversion_dec_to_bin(n):
    list = []
    while n > 0:
        list.append(n % 2)
        n = int(n / 2)
    list.reverse()
    list_to_string = ''.join(str(i) for i in list)
    print(f'Converted to binary: {list_to_string}')


conversion_dec_to_bin(num)

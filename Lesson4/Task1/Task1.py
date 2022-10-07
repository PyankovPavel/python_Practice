# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.


numbers = []
with open('file.txt') as file:
    read = file.readline()

list = read.split(' ')
for i in list:
    numbers.append(int(i))

print(numbers)
maximum = max(numbers)
minimum = min(numbers)

with open('3file.txt', 'w') as file:
    m = file.write(f'{maximum}  {minimum}')

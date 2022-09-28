# 3.	Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

str1 = input('Input string1: ')
str2 = input('Input string2: ')

string = ''
substring = ''

if len(str1) > len(str2):
    string = str1
    substring = str2
else:
    string = str2
    substring = str1


print(string.count(substring))






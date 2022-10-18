# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Пример:
#     "2+2" => 4;
#
#     "1+2*3" => 7;
#
#     "1-2*3" => -5;


str1 = '1+2*3'
print(eval(str1))

listNew = []
while True:
    for i in range(len(listNew)+1):
        if listNew[i] == "*":
            result = result + int(listNew[i-1]) * int(listNew[i+1])
            listNew = listNew.pop(listNew[i])

# Вычислить число c заданной точностью *d*
# Пример: при d = 0.001, π = 3.141; при d = 0.1, π = 3.1; при d = 0.00001, π = 3.14154; d от 0.1 до 0.0000000001

num = float(input('Input number to accurate: '))


def accuracy(n):
    lst = [0.1]
    for i in range(10):
        lst.append(lst[i] / 10)
    print(lst)
    while True:
        acc_rate = float(input('Input required accuracy from 0.1 до 0.0000000001: '))
        if acc_rate not in lst:
            print('Input correct accuracy')
        else:
            break
    count_of_round = 0
    while acc_rate < 1:
        acc_rate *= 10
        count_of_round += 1
    return round(n, count_of_round)


print(accuracy(num))

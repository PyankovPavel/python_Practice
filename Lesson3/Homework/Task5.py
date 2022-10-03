# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов [Негафибоначчи].
# Пример: для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Input number: '))


def solution(n):
    negafib = [0, 1] # тут будем собирать Негафибоначчи
    for i in range(n - 1):
        if i % 2 == 0 or i == 0:
            negafib.append((abs(negafib[i]) + negafib[i + 1]) * (-1))
        else:
            negafib.append(abs(negafib[i]) + abs(negafib[i + 1]))
    negafib.reverse()
    negafib.remove(0)
    st_fib = [0, 1] # тут будем собирать стандартный список Фибоначчи
    for i in range(n - 1):
        st_fib.append(((st_fib[i]) + st_fib[i + 1]))
    print(negafib + st_fib)


solution(num)

# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного,
# чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.

import random

# for i in range(1, 8)
list = [x for x in range(10)]
print(list)

list.pop(random.randint(1, len(list)-1))
print(list)

for i in range(1, len(list)):
    if list[i] - 1 != list[i-1]:
        print(i)


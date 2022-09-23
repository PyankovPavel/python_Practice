# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# /\ - AND, &, И, логическое умножение, конъюнкция
# \/ - OR, |, ИЛИ, логическое сложение, дизъюнкция
# ¬ - NOT, !,~, НЕ, отрицание, инверсия
# not(x or y or z) = notX and notY and notZ

def solution(x, y, z):
    return not (x or y or z) == (not x and not y and not z)


for x in range(2):
    for y in range(2):
        for z in range(2):
            print(solution(x, y, z))


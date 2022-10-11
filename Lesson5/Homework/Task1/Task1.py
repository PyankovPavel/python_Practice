# 2. Создайте программу для игры с конфетами человек против человека.
# Правила: На столе лежит 150 конфет. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'
import random

with open('Rules.txt', 'r') as rules:
    message = rules.read()
print(message)
sweets = int(input('Input number of sweets you wanna play: '))


def who_goes_first(flag):
    x = random.randint(1, 21)
    if flag == 'Human':
        print(f"Let's draw. If the number is even PlayerOne goes first, odd - PlayerTwo will begin."
              f"\nSo, the number is {x}")
        if x % 2 == 0:
            print('PlayerOne begins...')
            return True
        else:
            print('PlayerTwo begins...')
            return False
    else:
        print(f"Let's draw. If the number is even PlayerOne goes first, odd - AI will begin."
              f"\nSo, the number is {x}")
        if x % 2 == 0:
            print('PlayerOne begins...')
            return True
        else:
            print('AI begins...')
            return False


def appends_num(some_list: list):
    num = int(input())
    if 0 < num < 29:
        some_list.append(num)
    else:
        print(
            f"You try to take {num} sweets, it's wrong number. According the rules you can take no more than 28 sweets."
            f"Try again.")
        appends_num(some_list)


def game_with_human(n):
    flag = 'Human'
    player_one = []
    player_two = []
    index = 0
    while True:
        if who_goes_first(flag):
            while n > 0:
                print('PlayerOne how many sweets do you want? ')
                appends_num(player_one)
                n -= player_one[index]
                print(f'Amount of sweets on the table: {n}')
                if n == 0:
                    print('PlayerOne won')
                    break
                print('PlayerTwo how many sweets do you want? ')
                appends_num(player_two)
                n -= player_two[index]
                print(f'Amount of sweets on the table: {n}')
                if n == 0:
                    print('PlayerTwo won')
                index += 1
                break
        else:
            while n > 0:
                print('Player Two how many sweets do you want? ')
                appends_num(player_two)
                n -= player_two[index]
                print(f'Amount of sweets on the table: {n}')
                if n == 0:
                    print('Player Two won')
                    break
                print('Player One how many sweets do you want? ')
                appends_num(player_one)
                n -= player_one[index]
                print(f'Amount of sweets on the table: {n}')
                if n == 0:
                    print('Player One won')
                index += 1
            break


def ai_moves(some_list: list, n):
    if n > 57:
        some_list.append(random.randint(1, 28))
    elif 0 < n < 29:
        some_list.append(n)
    else:
        if n != 29:
            some_list.append(n - 29)
        else:
            some_list.append(random.randint(1, 28))


def game_with_ai(n):
    flag = 'ai'
    human = []
    ai = []
    index = 0
    while True:
        if who_goes_first(flag):
            while n > 0:
                print('Human how many sweets do you want? ')
                appends_num(human)
                n -= human[index]
                print(f'Amount of sweets on the table: {n}')
                if n == 0:
                    print('Human won')
                    break
                ai_moves(ai, n)
                print(f'AI taking {ai[index]} sweets ')
                n -= ai[index]
                print(f'Amount of sweets on the table: {n}')
                if n == 0:
                    print('AI won')
                index += 1
            break
        else:
            while n > 0:
                ai_moves(ai, n)
                print(f'AI taking {ai[index]} sweets ')
                n -= ai[index]
                print(f'Amount of sweets on the table: {n}')
                if n == 0:
                    print('AI won')
                    break
                print('Human how many sweets do you want? ')
                appends_num(human)
                n -= human[index]
                print(f'Amount of sweets on the table: {n}')
                if n == 0:
                    print('Human won')
                index += 1
            break


def select_play():
    num = input('Press 1 to play with another human or any symbol to play with bot: ')
    if num == '1':
        game_with_human(sweets)
    else:
        game_with_ai(sweets)

select_play()

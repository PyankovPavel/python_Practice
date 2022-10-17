# 2. Создайте программу для игры в крестики-нолики
import random


def fill_the_pitch():
    my_list = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
    return my_list


def print_the_pitch(some_list):
    print(f'{some_list[0]} \n{some_list[1]} \n{some_list[2]}'.replace('[', '').replace(']', '').replace(',', '')
          .replace("'", '|'))


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
            print('Player begins...')
            return True
        else:
            print('AI begins...')
            return False


def players_moves(some_table, player, some_set: set):
    if player != 'AI':
        n = int(input('Input number: '))
        some_set.add(n)
    else:
        while True:
            n = random.randint(1, 9)
            if n not in some_set:
                some_set.add(n)
                print(f'AI choose {n}')
                break
    if 0 < n < 4:
        index = 0
    elif 3 < n < 7:
        index = 1
    else:
        index = 2
    if player == 'PlayerOne':
        if str(n) not in some_table[index]:
            print(f'{n} was already entered before. Try another number')
            players_moves(some_table, 'PlayerOne', some_set)
        else:
            some_table[index] = [some_table[index][i].replace(f'{n}', 'X') for i in range(len(some_table[1]))]
            print_the_pitch(some_table)
    elif player == 'AI':
        some_table[index] = [some_table[index][i].replace(f'{n}', 'X') for i in range(len(some_table[1]))]
        print_the_pitch(some_table)
    else:
        if str(n) not in some_table[index]:
            print(f'{n} was already entered before. Try another number')
            players_moves(some_table, '', some_set)
        else:
            some_table[index] = [some_table[index][i].replace(f'{n}', 'O') for i in range(len(some_table[1]))]
            print_the_pitch(some_table)


def win_conditions(some_table: list, player):
    for i in range(3):
        if some_table[i] == ["X", "X", "X"]:
            print(f'{player} win!')
            return True
        elif some_table[i] == ["O", "O", "O"]:
            print('PlayerTwo win!')
            return True
        elif some_table[0][i] == "X" and some_table[1][i] == "X" and some_table[2][i] == "X":
            print(f'{player} win!')
            return True
        elif some_table[0][i] == "O" and some_table[1][i] == "O" and some_table[2][i] == "O":
            print('PlayerTwo win!')
            return True
        elif some_table[0][0] == "X" and some_table[1][1] == "X" and some_table[2][2] == "X":
            print(f'{player} win!')
            return True
        elif some_table[0][0] == "O" and some_table[1][1] == "O" and some_table[2][2] == "O":
            print('PlayerTwo win!')
            return True
        elif some_table[2][0] == "X" and some_table[1][1] == "X" and some_table[0][2] == "X":
            print(f'{player} win!')
            return True
        elif some_table[2][0] == "O" and some_table[1][1] == "O" and some_table[0][2] == "O":
            print('PlayerTwo win!')
            return True


def game_with_human():
    list_of_inputs = set()
    table = fill_the_pitch()
    print_the_pitch(table)
    flag = 'Human'
    player = 'PlayerOne'
    count = 1
    if who_goes_first(flag):
        while True:
            players_moves(table, player, list_of_inputs)
            if win_conditions(table, player):
                break
            if count > 8:
                print('Draw')
                break
            players_moves(table, '', list_of_inputs)
            if win_conditions(table, ''):
                break
            count += 2
    else:
        while True:
            players_moves(table, '', list_of_inputs)
            if win_conditions(table, ''):
                break
            if count > 8:
                print('Draw')
                break
            players_moves(table, player, list_of_inputs)
            if win_conditions(table, player):
                break
            count += 2


def game_with_ai():
    list_of_inputs = set()
    table = fill_the_pitch()
    print_the_pitch(table)
    flag = 'AI'
    player = 'PlayerOne'
    ai = 'AI'
    count = 1
    if who_goes_first(flag):
        while True:
            players_moves(table, '', list_of_inputs)
            if win_conditions(table, player):
                break
            if count > 8:
                print('Draw')
                break
            players_moves(table, ai, list_of_inputs)
            if win_conditions(table, flag):
                break
            count += 2
    else:
        while True:
            players_moves(table, ai, list_of_inputs)
            if win_conditions(table, flag):
                break
            if count > 8:
                print('Draw')
                break
            players_moves(table, '', list_of_inputs)
            if win_conditions(table, player):
                break
            count += 2


def select_play():
    num = input('Press 1 to play with another human or any symbol to play with bot: ')
    if num == '1':
        game_with_human()
    else:
        game_with_ai()


select_play()

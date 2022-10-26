import Model
import Controller


def view_of_phonebook():
    for i, item in enumerate(Model.phonebook):
        print(i, item)


def view_of_search(some_str: str):
    flag = False
    for i in range(len(Model.phonebook)):
        if Model.phonebook[i].__contains__(some_str.lower()):
            print(Model.phonebook[i])
            flag = True
    if not flag:
        inner_select = input('Данные не найдены. 1 - повторить поиск, иначе Главное меню ')
        if inner_select == '1':
            Controller.find_contact()
        else:
            Controller.main_menu()

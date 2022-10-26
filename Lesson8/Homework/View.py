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
            main_menu()


def main_menu():
    while True:
        print('\nГлавное меню:')
        print('0. Открыть файл с контактами')
        print('1. Добавить контакт')
        print('2. Удалить контакт')
        print('3. Изменить контакт')
        print('4. Показать все контакты, в т.ч. несохраненные')
        print('6. Поиск по контактам')
        print('8. Сохранить файл')
        print('9. Закрыть программу')
        select = int(input('Выберите пункт: '))
        match select:
            case 0:
                Controller.open_file()
                view_of_phonebook()
            case 1:
                Controller.add_contact()
                print('\nКонтакт добавлен\n')
            case 2:
                Controller.remove_contact()
                print('\nКонтакт удален\n')
            case 3:
                Controller.change_contact()
            case 4:
                Controller.show_unsaved_contacts()
            case 6:
                Controller.find_contact()
            case 8:
                Controller.save_file()
                print('\nФайл сохранен!\n')
            case 9:
                exit()

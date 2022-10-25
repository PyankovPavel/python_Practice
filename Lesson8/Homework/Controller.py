import Model
import View


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
                open_file()
                View.view_of_phonebook()
            case 1:
                add_contact()
                print('\nКонтакт добавлен\n')
            case 2:
                remove_contact()
                print('\nКонтакт удален\n')
            case 3:
                change_contact()
            case 4:
                show_unsaved_contacts()
            case 6:
                find_contact()
            case 8:
                save_file()
                print('\nФайл сохранен!\n')
            case 9:
                exit()


def start_app():
    main_menu()


def open_file():
    with open(Model.path, "r", encoding="UTF-8") as file:
        contacts_list = file.read().split("\n")
        Model.phonebook = contacts_list


def save_file():
    with open(Model.path, "w", encoding="UTF-8") as file:
        file.write(('\n'.join(Model.phonebook)))


def add_contact():
    name = input('Введите имя: ')
    middle_name = input('Введите отчество, если есть: ')
    surname = input('Введите фамилию: ')
    phone = input('Введите телефон: ')
    contact = f'{name}; {middle_name}; {surname}; {phone};'
    Model.phonebook.append(contact.lower())
    View.view_of_phonebook()
    save_select = input('Сохранить изменения? Введите 1 или y, иначе -  нет ')
    if save_select == '1' or save_select == 'Y'.lower():
        save_file()
    else:
        main_menu()


def remove_contact():
    select = int(input('Введите номер элемента для удаления: '))
    Model.phonebook.pop(select)
    View.view_of_phonebook()


def change_contact():
    select = int(input('Введите номер элемента для изменения: '))
    changes = int(input('Что изменяем (0-имя, 1-отчество, 2-фамилия, 3-телефон): '))

    contact = Model.phonebook.pop(select).split(';')
    print(contact)
    contact[changes] = input('Введите новое значение: ')
    print(contact)
    Model.phonebook.insert(select, ';'.join(contact).lower())
    View.view_of_phonebook()
    save_file()


def show_unsaved_contacts():
    for i in Model.phonebook:
        print(i)


def find_contact():
    open_file()
    select = int(input('По какому параметру будем искать? (0-имя, 1-отчество, 2-фамилия, 3-телефон): '))
    flag = False
    match select:
        case 0:
            name = input(f'Введите искомое имя: ') + ';'
            for i in range(len(Model.phonebook)):
                if Model.phonebook[i].__contains__(name.lower()):
                    print(Model.phonebook[i])
                    flag = True
            if not flag:
                inner_select = input('Данные не найдены. 1 - повторить поиск, иначе Главное меню')
                if inner_select == '1':
                    find_contact()
                else:
                    main_menu()
        case 1:
            middle_name = input(f'Введите искомое отчество: ') + ';'
            for i in range(len(Model.phonebook)):
                if Model.phonebook[i].__contains__(middle_name.lower()):
                    print(Model.phonebook[i])
                    flag = True
            if not flag:
                inner_select = input('Данные не найдены. 1 - повторить поиск, иначе Главное меню')
                if inner_select == '1':
                    find_contact()
                else:
                    main_menu()
        case 2:
            surname = input(f'Введите искомую фамилию: ') + ';'
            for i in range(len(Model.phonebook)):
                if Model.phonebook[i].__contains__(surname.lower()):
                    print(Model.phonebook[i])
                    flag = True
            if not flag:
                inner_select = input('Данные не найдены. 1 - повторить поиск, иначе Главное меню')
                if inner_select == '1':
                    find_contact()
                else:
                    main_menu()
        case 3:
            surname = input(f'Введите искомый телефон: ') + ';'
            for i in range(len(Model.phonebook)):
                if Model.phonebook[i].__contains__(surname.lower()):
                    print(Model.phonebook[i])
                    flag = True
            if not flag:
                inner_select = input('Данные не найдены. 1 - повторить поиск, иначе Главное меню')
                if inner_select == '1':
                    find_contact()
                else:
                    main_menu()

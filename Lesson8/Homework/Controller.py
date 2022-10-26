import Model
import View


def start_app():
    View.main_menu()


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
        View.main_menu()


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
    match select:
        case 0:
            name = input(f'Введите искомое имя: ') + ';'
            View.view_of_search(name)
        case 1:
            middle_name = input(f'Введите искомое отчество: ') + ';'
            View.view_of_search(middle_name)
        case 2:
            surname = input(f'Введите искомую фамилию: ') + ';'
            View.view_of_search(surname)
        case 3:
            number = input(f'Введите искомый телефон, формат 79213214567: ') + ';'
            View.view_of_search(number)

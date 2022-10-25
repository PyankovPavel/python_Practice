import Model


def view_of_phonebook():
    for i, item in enumerate(Model.phonebook):
        print(i, item)

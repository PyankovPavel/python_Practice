import controller
import view
import eq_one_str

first = 0
second = 0
ops = ''
total = 0
select: str


def select_calc():
    global select
    global first
    select = input('Какой  режим калькулятора запустить? 1 - в одну строку, '
                   'в ином случае запуститься поэлементный ')
    while True:
        if select == "1":
            eq_one_str.start_eq()
            y = input('Продолжаем вычисления? Напишите y или да, если хотите продолжить, '
                      'в ином случае программа завершится ')
            if y.lower() == 'y' or y.lower() == 'да':
                continue
            else:
                break
        else:
            print('Следуйте инструкции, для завершения ввести "=" в консоль')
            init_first()
            while True:
                if init_ops():
                    break
                init_second()
                controller.operation()
                view.print_total()
                first = total
            break


def init_first():
    global first
    first = controller.input_integer('Введите число: ')


def init_second():
    global second
    second = controller.input_integer('Введите число: ')


def init_ops():
    global ops
    ops = controller.input_operation('Введите операцию: ')
    if ops == '=':
        view.print_total()
        return True

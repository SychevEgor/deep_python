import datetime
"""
bank = 0
count = 0
percent_take = 0.015
percent_add = 0.03
percent_tax = 0.01

def add_bank(cash: float) -> None:
    global bank
    global count
    bank += cash
    count += 1
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Зачисленные проценты: ", percent_add * bank)

def take_bank(cash: float) -> None:
    global bank
    global count
    bank -= cash
    count += 1

    if cash * percent_take < 30:
        bank -= 30
        print("Списаные проценты:  ", 30)
    elif cash * percent_take > 600:
        bank -= 600
        print("Списаные проценты: ", 600)
    else:
        bank -= cash * percent_take
        print("Списаные проценты: ", cash * percent_take)
    if count % 3 == 0:
        bank = bank + percent_add * bank
        print("Зачисленые проценты: ", percent_add * bank)


def exit_bank():
    print("Вам одобрен кредит, подробнее по сайту www.washcredit.com\n")
    exit()

def check_bank() -> int:
    while True:
        cash = int(input("Введите сумму опреации кратно 50\n"))
        if cash % 50 == 0:
            return cash

list_operation = []

while True:
    action = input("1 - снять деньги\n2 - пополнить\n3 - баланс\n4 - вывести историю операций\n5 - выйти\n")

    if action == '1':
        cash = check_bank()
        if cash < bank:
            take_bank(cash)

            list_operation.append([str(date.today()), -1 * cash])
        else:
            print("Нечего снимать\nБаланс ", bank)
    elif action == '2':
        cash = check_bank()
        add_bank(cash)

        list_operation.append([str(date.today()), cash])

    elif action == '3':
        print("Баланс = ", bank)
    elif action == '4':
        print(list_operation)
    else:
        exit_bank()
"""
"""
def dictionary_creator(**kwargs):
    returned_dict = dict()
    for k, v in kwargs.items():
        try:
            returned_dict[v] = k
        except Exception:
            returned_dict[str(v)] = k
    return returned_dict


print(dictionary_creator(name='Igor', current_date=str(datetime.datetime.now())))
"""
import random


def transportation_matrix (list):
    transportation_matrix = []
    for i in range(len(list)):
        transportation_matrix_dem = []
        for j in range(len(list[i])):
            transportation_matrix_dem.append(list[j][i])
        transportation_matrix.append(transportation_matrix_dem)
    return transportation_matrix


def print_mat (list, word):
    print(word)
    for row in list:
        print(*row)


matrix = [[random.randint(1, 10) for _ in range(4)] for _ in range(4)]
print_mat(matrix, 'Созданная матрица:')
trans_mat = transportation_matrix(matrix)
print_mat(trans_mat, 'Транспонированная матрица:')
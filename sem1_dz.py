import random

"""
a = int(input("Введи a"))
b = int(input("Введи b"))
c = int(input("Введи c"))
if a < b + c and b < a + c and c < a + b:
    print("Да , это треугольник")
    if a == b == c:
        print("Равносторонний")
    elif a == b or b == c or c == a or a == c:
        print("Равнобедренный")
    elif a != b and b != c and c != a:
        print("Разносторонний")
else:
    print("Это не треугольник!")

while True:
    user_num = int(input("Введите число не больше 100 000 и не отрицательное"))
    print()
    if user_num > 100000 or user_num < 0:
        print("Не соответсвует условию, перезапуск...")
        continue
    else:
        TWO_CONST = 2
        while TWO_CONST <= user_num - 1:
            if user_num % TWO_CONST == 0:
                break
            else:
                TWO_CONST +=1
        if user_num == 1 or TWO_CONST == user_num:
            print("Число простое")
        else:
            print("Число составное")

"""
random_numbers = random.randint(0, 1000)
count = 0

while count <= 10:
    count += 1
    user_number = int(input("Введите какое число загадала програма: "))
    print("Попытка номер " + str(count))
    if user_number == random_numbers:
        print("Вы победили!")
        break
    else:
        if user_number < random_numbers:
            print("больше")
            continue
        else:
            print('меньше')
            continue

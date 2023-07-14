"""
user_number = int(input('введите число'))
result = ''
hex_list = '0123456789ABCDEF'

while user_number > 0:
    result = hex_list[user_number % 16] + result
    user_number //= 16
print(result)
"""
from fractions import Fraction as F
global res


def fraction(user_number_1, user_number_2, operation):
    user_number_1 = F(user_number_1).limit_denominator(10)
    user_number_2 = F(user_number_2).limit_denominator(10)
    if operation in ('+', '-', '*', '/'):
        if operation == '+':
            res = user_number_1 + user_number_2
        elif operation == '-':
            res = user_number_1 - user_number_2
        elif operation == '*':
            res = user_number_1 * user_number_2
        elif operation == '/':
            res = user_number_1/user_number_2

    if res.numerator > res.denominator:
        while res.numerator > res.denominator:
            find_whole_part = (res.numerator // res.denominator)
            find_numerator = res.numerator % res.denominator
            push_itog = f'{res} = {find_whole_part} {find_numerator}/{res.denominator}'
            res = f'{user_number_1} {operation} {user_number_2} = {push_itog}'
            return res
    else:
        res = f'{user_number_1} {operation} {user_number_2} = {res}'
        return str(res)
s = fraction(1/3,1/5,'+')
print(s)
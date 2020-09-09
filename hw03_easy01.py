#!/usr/bin/env python
__author__ = ''
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(my_num, my_digits):

    return float(my_num).__round__(my_digits)

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_nr):
    first_part = ticket_nr // 1000
    second_part = ticket_nr % 1000

    def part_sum(num):
        part_sum = 0
        while num > 0:
            part_sum += num % 10
            num //= 10
        return part_sum
    if part_sum(first_part) == part_sum(second_part):
        result = 'Lucky'
    else:
        result = 'Unlucky'
    return result


def main():
    print(my_round(2.1234567, 5))
    print(my_round(2.1999967, 5))
    print(my_round(2.9999967, 5))
    print(lucky_ticket(123060))
    print(lucky_ticket(123080))


if __name__ == '__main__':
    main()

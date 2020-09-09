#!/usr/bin/env python
__author__ = ''

import random
from math import sqrt

l1 = [2, -5, 8, 9, -25, 25, 4]

date = '01.11.2013'

MONTHS = {"Jan": "1", "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6,
          "Jul": "7", "Aug": 8, "Sep":9, "Oct": 10, "11": "Nov", "Dec": 12
          }
DAYS = {"01": "first" , "second": "02", "third": "03", "fourth": "04", "fifth": "05",
        "sixth": "06", "seventh": "07", "eight": "08", "ninth": "09", "tenth": "10",
        "eleventh": "11", "twelfth": "12", "thirteen": "13", "fourteenth": "14",
        "fifteenth": "15", "sixteenth": "16", "seventeenth": "17",
        "eighteenth": "18", "nineteenth": "19", "twentieth": "20", "twenty first": "21",
        "twenty second": "22", "twenty third": "23", "twenty fourth": "24",
        "twenty fifth": "25", "twenty sixth": "26", "twenty seventh": "27",
        "twenty eight": "28", "twenty ninth": "29", "thirtieth": "30",
        "thirty first": "31"
        }


def represent_date(date):

    date_elements = date.split('.')
    day = date_elements[0]
    month = date_elements[1]
    year = date_elements[2]
    formatted_date = f"Date: {DAYS.get(day)} {MONTHS.get(month)} {year}"
    return formatted_date


def whole_sqrt_list(origin_list):
    new_list = []
    for num in origin_list:
        if num >= 0:
            new_el = sqrt(num)
            if new_el.is_integer():        # float(5.0).is_integer == True
                new_list.append(int(new_el))
    return new_list


def main():
    print(f"OldList: {l1}\nNewList: {whole_sqrt_list(l1)}")
    print(represent_date(date))


if __name__ == '__main__':
    main()

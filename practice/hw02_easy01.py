#!/usr/bin/env python
__author__ = ''

l1 = ["яблоко", "банан", "киви", "арбуз"]

l2 = ["1", "two", "three", "3", "2"]
l3 = ["one", "two", "3"]

l4 = [7, 2, 1, 9, 1, 0, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 2, 3, 4, 5]


def half_odd_dbl_even(some_list):
    new_list = []
    for num in some_list:
        if num % 2 == 0:
            new_list.append(num / 4)
        else:
            new_list.append(num * 2)
    return new_list


def cleanup(list1, list2):

    for el1 in list2:
        if el1 in list1:
            list1.pop(list1.index(el1))
    return list1


def el_width(some_list):
    width = 0
    for el in some_list:
        if len(el) > width:
            width = len(el)
    return width


def main():
    width = el_width(l1)
    i = 0
    for el in l1:
        print(f"{i}. {el:>{width}}")
        i += 1

    print(f"Remove occurrences of {l3} in {l2}\nResult: {cleanup(l2,l3)}")
    print(f"OldList: {l4}, \nNewList: {half_odd_dbl_even(l4)}")


if __name__ == '__main__':
    main()

#!/usr/bin/env python
__author__ = ''


def main():
    pass


if __name__ == '__main__':
    main()

# functions
# print()
# input()
# len()
# int(), float(), bool()
# range(start, stop, step)
# abs(x)
# max(x, y) min(x)
# round(x,n) n to which symbol after dot we need rounding
# type()
# enumerate()  returns element and index position

# named functions :
# def f_name(*args): args = tuple of elements (unnamed arguments)
#   s = 0
#   for arg in args:
#       s += arg
#   return s / len(args)
# functions :
# def f_name(**kwargs): # kwargs = dictionary of elements (named arguments)
#     print(f"Your name: { kwargs['name'] }, Your age: { kwargs['age']}")
#
# f_name(name="viktor", age=20)

# one can define functions with defaults arguments:
# def f_name(name="default value"):
#     print(f"Your name: { name }")
# f_name()

# lambda functions
# lambda arguments: expression
# add = lambda x,y: x + y
# add(2,3)
# 5
# sorted(iterable, /, *, key=None, reverse=False)
# Return a new list containing all items from the iterable in ascending order.
# A custom key function can be supplied to customize the sort order, and the
# reverse flag can be set to request the result in descending order.

# mainly used for sorting :
# sorted(range(-5,6))
# vs:
# sorted(range(-5,6), key = lambda x: x**2)
# will sort numbers in range from -5 to 5 by their power of 2
# [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5] will become [0, -1, 1, -2, 2, -3, 3, -4, 4, -5, 5]
# -1 in power of 2 will become 1
# so sort will place -1 and 1 right after 0

# zip(a,b) - joins arguments (arguments must be iterable) into tuples
# if one of arguments lacks elements, this element will be skipped
# a = [1, 2]
# b = [3, 4]
# print(list(zip(a,b))
# a = [1, 2, 7]
# h = [4,5]
# b = [3, 4, 9]
# print(list(zip(a,h,b))

# class map(object)
#    map(func, *iterables)
# for example we need a list, where each element would be doubled
# lambda function is handy to do this x will take value of list element
# print(list(map(lambda x: x*x, [2,3,-90,34])))

# filter() removes elements to which function returns false
# returns iterable object
# filter(func, *iterable)
# print(list(filter(lambda x: x>5, [2,10,11,3,0,False,True])))
# print(tuple(filter(len, ['',"aag2f","","gs"])))
# print(tuple(filter(lambda x: len(x) > 3, ['',"aag2f","","gs"])))
# print(list(filter(lambda x: len(x) > 3, ['',"aag2f","","gs"])))


# to work with files nee 2 libraries os and sys
# import os
# import sys
# path = os.path.join("files", "text.txt")
# f = open(path, "r", encoding="UTF-8")
# print(f.readlines())
# f.close()
# my_file = open("some.txt", "w")
# my_file.write("bur bur bur \ very much.
# my_file.close()



#!/usr/bin/env python
__author__ = ''


def main():
    pass


if __name__ == '__main__':
    main()

# slice is object which contains list of indexes
# slice(start index, stop index, step)
# lol = 'long string'
# l o n g  s t r i n g
# 0                 -1
# lol[2:5] from 2nd index till 4TH index (5th index being excluded)
# lol[2:] from 2nd index till the end
# lol[:17] from 0 index till 16 index
# lol[-4:] last 4 symbols
# lol[:-4] all except last 4 symbols
# lol[::2] symbol under 0 index + symbols in each 2nd index after index0

# alt='0123456789abcdef'
# string methods
# string.title() will make char under index 0 as uppercase, all other as lower
# string.upper() all upper case
# string.find(sub, start, end) return index where "sub" where found in slice
# returns -1 if sub was not found
# alt.find("a", -6) will return 10 (an index of a position in original string)

# String formatting
# age = 25, name="katerina"
# print("%s. %d"%(name, age)) %s for string, %d for digits
# Katerina. 25

# print("{}. {}}".format(name, age))
# print("{}. {}}".format(age, name))
# print("{1}. {0}}".format(age, name)) 0 is age 1 is name

# f strings:
# print(f"{ age }. { name }")
# from math import pi
# print(f"pi: {pi:.2f}")  .2f - digits after dot
# from

# lists - are ordered, changeable collection of any type objects
# empty_list = []
# one can use slices with lists
# my_list = [1,2,3,4,6.897, 'asafs', False]
# my_list[-1] will return False (the last element in list)
# my_list[:3]
# my_list[:-3]
# concatenation of list
# my_list[:3] + [7,8,9]  will return new list, original list will not be changed
# [3, "5"] * 3
# my_list[2] = "TT" changes original list, set 2nd element value TT
# edit list with slice:
# my_list[:3] = [3,4,5]  replace elements under indexes 0,1,2 with values 3,4,5
# my_list[3:3] = ["one", "two", "three"] insert 3 list elements from 3rd index
# my_list[:0] = ["foo"] vill insert foo under index0
# my_list[:0] = "foo" will insert "f" "o" "o" at 0,1,3 rd indexes
# my_list[len(my_list):] = [100]  append 100 to the list
# my_list[-1:] = [] will remove last element from list
# list mehods:
# my_list.append(9) will append 9 to list
# my_list.pop() will cut last element
# my_list.pop(3) will remove element from position under index3
# b = [1,2,3,[11,22,33],4,5]
# b[3][0] will return 11 (list inside list)


# tuple immutable ordered collection of items
# t1 = (2,)

# while len(fruits) > i:
#   print(f"fruits: { fruits[i] }")
#   i += 1
# for fruit in fruits:
#     print(f"Fruits: { fruit }")

# dictionaries unordered collection of key:value objects
# d1 = dict()
# d2 = {}
# d3 = {"Key1": "Val1", "Key3": 123}
# d1["City"] = "moscow" will append to d1 key "Cyti" with value "moscow"
# to remove key from d1 use del
# del d3["Key3"]
# keys within dictionary should be unique
# d4 = {"r": 5, "r", 236} will contain 1 r key with value 236
# "Key1" in d3.keys() will return true if "Key1" is found in d3 key list
# "Key1" in d3 will return true if "Key1" is found in d3 key list
# "Val1" in d3.values() will return true if "Key1" is found in d3 key list
#
# dictionary methods
# d3.get("Key1") will return key1 value
# d3.items() will return list of items (key:,val)
# d3.keys() will return list of keys
# d3.values() will return list of values


# Sets unordered collection of unique objects
# s = set()
# s = set(["a","b","a","c","t","c","a","y"])
# s2 = set("hello")
# {'e', 'l', 'h', 'o'}
# frozenset

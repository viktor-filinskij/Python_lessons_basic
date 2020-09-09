#!/usr/bin/env python
__author__ = ''


def main(x=abs(int(input("Enter whole number: ")))):
    # number = abs(int(input("Enter whole number: ")))
    number = x
    max_digit = 0

    while number !=0:
        if number % 10 > max_digit:
            max_digit = number % 10
        number //= 10
    print(f"biggest digit: { max_digit }")


if __name__ == '__main__':
    main()

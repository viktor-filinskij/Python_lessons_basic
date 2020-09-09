#!/usr/bin/env python
__author__ = ''


def main(a=input("Enter a: "), b=input("Enter b: "), c=input("Enter c: ")):
    # a(x^2) + bx + c = 0 when a !=0, b !=0, c !=0
    # d = b ** 2 - 4 * a * c
    # if d > 0  x(1,2) = (-b (+/-) sqrt(d)) / 2a
    # if d = 0  x = - ( b / 2 * a)
    # if d < 0  x(1,2) = ( -b / 2a ) (+/-) i(sqrt(abs(d)) / 2a)
    d = b ** 2 - 4 * a * c

    pass


if __name__ == '__main__':
    main()

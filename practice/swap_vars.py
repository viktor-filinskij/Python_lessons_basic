#!/usr/bin/env python
__author__ = ''


def main(x=input("Enter first var: "), y=input("Enter second var: ")):
    x, y = y, x
    print(f"first var = { x }, second var = { y }")


if __name__ == '__main__':
    main()

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
----------------------------------------
    Filename   : Console.py
    Description: Console drawing tool.
    Author     : XSky123
    Created at : 2017/11/21 12:01
----------------------------------------
"""
__LINE_1__ = "========================================"
__LINE_2__ = "****************************************"
__LINE_3__ = "----------------------------------------"


def line(style=1, length=40):
    """ draw line with print.

    :param style:
        1 -> 40 x '='
        2 -> 40 x '*'
        3 -> 40 x '-'

    :param length:
    """
    l = ""
    if style == 1:
        for i in range(length):
            l += "="

    elif style == 2:
        for i in range(length):
            l += "*",

    elif style == 3:
        for i in range(length):
            l += "-"

    print(l)


def menu(choices):
    """ show choices and do basic check.
    if not correct input, keep retrying.

    show choice number begins at 1,
    but return number begins at 0.

    return choice as number( from 0 )
    """
    # show choices
    line(length=30)
    for i, choice in enumerate(choices):
        print("[%d] %s" % (i+1, choice))
    line(length=30)
    while True:
        choice = int(input("  Input: "))
        if 0 < choice <= len(choices):
            break

    return choice-1


def input_c(tips):  # input  confirm
    while True:
        tmp = input("* {}: ".format(tips))
        if tmp == "":
            confirm = input("Your input is nothing. [y] to confirm: ")
        else:
            confirm = input("Your input is {}. [y] to confirm: ".format(tmp))
        if confirm == "y":
            return tmp
        else:
            print("Retry.")


def input_b(tips): # input bool
    tmp = input("* {}? [y] for yes. [other] for no".format(tips))
    if tmp == "" or tmp == "y":
        return True
    return False


def main():
    pass


if __name__ == '__main__':
    main()

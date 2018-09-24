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


def input_r(tips):
    ''' input with back view'''
    tmp = input("* {} > ".format(tips))
    if tmp == "":
        confirm = "nothing"
    else:
        confirm = tmp

    print("> {}".format(confirm))
    return tmp


def input_c(tips):
    ''' input and confirm'''
    while True:
        tmp = input("* {} > ".format(tips))
        if tmp == "":
            confirm = input("> nothing\n> press [Enter] to confirm > ")
        else:
            confirm = input("> {}\n> press [Enter] to confirm > ".format(tmp))
        if confirm == "" or confirm == "y":
            return tmp
        else:
            print("* Retry")


def input_b(tips): 
    ''' input bool '''
    tmp = input("* {}?\nInput [y] for yes > ".format(tips))
    if tmp == "" or tmp == "y":
        return True
    return False


def main():
    pass


if __name__ == '__main__':
    main()

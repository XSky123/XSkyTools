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
    if style == 1:
        for i in range(length):
            print '=',
        print '\n'

    elif style == 2:
        for i in range(length):
            print '*',
        print '\n'

    elif style == 3:
        for i in range(length):
            print '-',
        print '\n'


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
        print "  [%d] %s" % (i+1, choice)
    line(length=30)
    while True:
        choice = int(raw_input("  Input: "))
        if 0 < choice <= len(choices):
            break

    return choice-1


def main():
    pass


if __name__ == '__main__':
    main()

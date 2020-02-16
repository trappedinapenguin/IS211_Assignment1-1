#!/usr/bin/env python
# -*- coding: utf-8 -*-

def listDivide(number=[], divide=2):
    count = 0
    for item in number:
        try:
            if (item % divide == 0):
                count = count + 1
        except:
            if divide == 0:
                raise ListDivideException(ZeroDivisionError)

    return count


class ListDivideException(ZeroDivisionError):
    pass


def testListDivide(listDivide):
    try:
        testListDivide
    except (ListDivideException):
        raise ListDivideException(ZeroDivisionError)


testListDivide(listDivide([1, 2, 3, 4, 5]))
testListDivide(listDivide([2, 4, 6, 8, 10]))
testListDivide(listDivide([30, 54, 63, 98, 100], divide=10))
testListDivide(listDivide([]))
testListDivide(listDivide([1, 2, 3, 4, 5], 1))

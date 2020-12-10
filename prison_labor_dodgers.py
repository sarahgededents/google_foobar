import functools
import operator


def solution1(x, y):
    return functools.reduce(operator.xor, x+y)
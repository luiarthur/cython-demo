from cython import double
from cython import int as cint


def add_numbers(n: cint) -> double:
    out: double = 0.0
    i: cint
    for i in range(n):
        if i < n / 2:
            out += i
        else:
            out += i / 2
    return out

from time import perf_counter

from cython_tests.boo import add_numbers_slowly
from cython_tests.wow import add_numbers


def run(f, n):
    tic = perf_counter()
    out = f(n)
    toc = perf_counter()
    print(f"Computed {out} in {toc-tic} seconds.")


if __name__ == "__main__":
    n = 1_000_000
    run(add_numbers, n)
    run(add_numbers_slowly, n)

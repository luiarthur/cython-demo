from time import perf_counter

from cython_tests.boo import add_numbers_slowly
from cython_tests.wow import add_numbers
from compiled_stuff import add_numbers as compiled_add_numbers


def run_and_time(name: str, f, *args, **kwargs):
    tic = perf_counter()
    out = f(*args, **kwargs)
    toc = perf_counter()
    print(f"{name}: Computed {out} in {toc-tic} seconds.")


if __name__ == "__main__":
    n = 1_000_000
    run_and_time("add_numbers", add_numbers, n)
    run_and_time("add_numbers_compiled", compiled_add_numbers, n)
    run_and_time("add_numbers_slowly", add_numbers_slowly, n)

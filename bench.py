from time import perf_counter

from cython_demo.functions import add_numbers
from fast import add_numbers as add_numbers_fast


def run_and_time(name: str, f, *args, **kwargs):
    tic = perf_counter()
    out = f(*args, **kwargs)
    toc = perf_counter()
    print(f"{name}: Computed {out} in {toc-tic} seconds.")


if __name__ == "__main__":
    n = 1_000_000
    run_and_time("add_numbers", add_numbers, n)
    run_and_time("add_numbers_fast", add_numbers_fast, n)

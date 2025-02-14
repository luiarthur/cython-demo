from time import perf_counter

from cython_demo.slow import add_numbers
from cython_demo.fast import add_numbers as add_numbers_fast


def run_and_time(name: str, f, *args, **kwargs):
    tic = perf_counter()
    result = f(*args, **kwargs)
    toc = perf_counter()
    wall = toc - tic
    msg = f"{name}: Computed {result} in {toc-tic} seconds."
    return dict(result=result, wall=wall, msg=msg)


def test_times():
    n = 1_000_000
    info_slow = run_and_time("add_numbers", add_numbers, n)
    info_fast = run_and_time("add_numbers_fast", add_numbers_fast, n)
    assert info_slow["result"] == info_fast["result"]
    assert info_fast["wall"] * 10 < info_slow["wall"]
    print()
    print(info_slow["msg"])
    print(info_fast["msg"])

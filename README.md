# Cython Demo

Demo of using cython in a package.

## Installation

**pip**
```
pip install git+ssh://git@github.com/luiarthur/cython-demo.git
```

**uv**
```
uv add git+https://github.com/luiarthur/cython-demo.git
```

## Run benchmarks
```
just t
```

## Demo
```python
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


n = 1_000_000
info_slow = run_and_time("add_numbers", add_numbers, n)
info_fast = run_and_time("add_numbers_fast", add_numbers_fast, n)

print(info_slow['msg'])
#> add_numbers: Computed 312499625000.0 in 0.07007383409328759 seconds.

print(info_fast['msg'])
#> add_numbers_fast: Computed 312499625000.0 in 0.0016072089783847332 seconds.
```

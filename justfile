name := "cython_demo"
alias c := clean
alias r := run
alias b := build

@default:
  just -l

run:
  uv run python bench.py

build: clean
  uv run python -m build

clean:
  rm -rf src/{{name}}/__pycache__
  rm -f src/{{name}}/*.c
  rm -rf src/*.egg-info
  rm -f src/*.so
  rm -rf dist

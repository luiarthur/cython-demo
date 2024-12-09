alias r := run
alias b := build

@default:
  just -l

run:
  uv run python bench.py

build:
  uv run python -m build

name := "cython_demo"

alias c := clean
alias t := test
alias b := build
alias f := fmt

@default:
    just -l

test:
    uv run pytest -s

build: clean
    uv run python -m build

clean:
    rm -rf src/{{ name }}/__pycache__
    rm -f src/{{ name }}/*.c
    rm -rf src/*.egg-info
    rm -f src/*.so
    rm -rf dist

fmt:
    ruff format
    just --fmt --unstable

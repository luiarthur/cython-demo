name := "cython_demo"

alias c := clean
alias t := test
alias b := build
alias f := fmt
alias h := help

# Print this help menu.
help:
    just -l

# Run benchmark.
test:
    uv run pytest -s

# Compile cython code.
build: clean
    uv run python -m build

# Remove compiled files.
clean:
    rm -rf src/{{ name }}/__pycache__
    rm -f src/{{ name }}/*.c
    rm -rf src/*.egg-info
    rm -f src/*.so
    rm -rf dist

# Format python modules and this justfile.
fmt:
    ruff format
    just --fmt --unstable

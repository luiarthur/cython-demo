name := "cython_demo"

alias c := clean
alias t := test
alias f := fmt
alias h := help

# Print this help menu.
help:
    just -l

# Run benchmark.
test:
    uv run pytest -s

# Remove compiled files.
clean:
    rm -rf tests/__pycache__
    rm -rf src/{{ name }}/__pycache__
    rm -f src/{{ name }}/*.c
    rm -rf src/*.egg-info
    rm -rf dist
    rm -f src/{{ name }}/*.so

# Format python modules and this justfile.
fmt:
    ruff format
    just --fmt --unstable

# Rebuild and reinstall compiled cython modules. 
reinstall:
    uv run --reinstall-package={{ name }} -- echo

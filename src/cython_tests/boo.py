def add_numbers_slowly(n: int):
    out = 0.0
    for i in range(n):
        if i < n / 2:
            out += i
        else:
            out += i / 2
    return out

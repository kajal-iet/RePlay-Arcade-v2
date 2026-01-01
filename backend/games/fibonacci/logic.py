from functools import lru_cache

@lru_cache(maxsize=None)
def fib_safe(n: int):
    if n <= 1:
        return n
    return fib_safe(n - 1) + fib_safe(n - 2)

def fib_fast(n: int):
    if n == 1:
        return 0
    if n == 2:
        return 1
    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

def build_timeline(n: int):
    seq = []
    a, b = 0, 1
    seq.append(a)
    if n > 1:
        seq.append(b)
    for _ in range(3, n + 1):
        a, b = b, a + b
        seq.append(b)
    return seq

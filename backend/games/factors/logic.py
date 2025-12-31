import math

def find_factors(n: int):
    factors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)

    factors.sort()
    return {
        "number": n,
        "factors": factors,
        "is_prime": len(factors) == 2
    }

def bang(x: int) -> int:
    res: int = 1
    for i in range(1, x + 1, 1):
        res *= i
    return int(res)

def combination(n: int, x: int) -> int:
    return int(bang(n) / (bang(x)*bang(n - x)))

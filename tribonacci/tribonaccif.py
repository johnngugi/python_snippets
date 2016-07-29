def tribonacci(n):   # return Fibonacci series up to n
    result = []
    a, b,c = 0,0, 1
    while b < n:
        result.append(b)
        a, b, c = b, c, a + b + c
    return result
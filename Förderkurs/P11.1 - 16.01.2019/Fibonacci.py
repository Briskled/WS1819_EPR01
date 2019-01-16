def fib_rek_bad(n):
    """The bad recursive implementation for calculating the n-th fibonacci number"""
    
    if n == 1 or n == 2:
        return 1
    return fib_rek_bad(n-1) + fib_rek_bad(n-2)


def fib_rek_good(n, a=0, b=1):
    """The good recursive implementation for calculating the n-th fibonacci number
    There will be no runtime issues"""
    
    if n == 1:
        return a + b
    return fib_rek_good(n-1, a + b, a)



def fib_iter(n):
    """A iterative implementation for calculating the n-th fibonacci number
    There will be no runtime issues."""
    
    b = 0
    a = 1
    for i in range(n):
        b = a + b
        a, b = b, a
    return b











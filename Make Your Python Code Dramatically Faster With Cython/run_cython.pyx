cpdef long fastfactorial(long n):
    if  n >= 1:
        return n * fastfactorial(n - 1)
    return 1
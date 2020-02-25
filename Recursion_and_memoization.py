# Recusive functions utilizing memoization for faster computing
# Memoization: cache results so they dont have to be caluclated again

cache = {}
def fibonacci(n):
    # Verify 'n' is both an Intiger & greater than 0
    if type(n) != int:
        raise TypeError("Must be an Intiger")
    elif n < 1:
        raise ValueError("Number must be greater than 0")
    else:
        if n in cache:
            return cache[n]

        if n <= 2:
            value = 1
        elif n > 2:
            value = fibonacci(n-1) + fibonacci(n-2)

        cache[n] = value
        return value


def factorial(n):
    # Verify 'n' is both an Intiger & greater than 0
    if type(n) != int:
        raise TypeError("Must be an Intiger")
    elif n < 0:
        raise ValueError("Number must be greater than 0")
    else:
        if n in cache:
            return cache[n]

        if n == 1:
            value = 1
        elif n == 2:
            value = 2
        elif n > 2:
            value = n * factorial(n-1)

        cache[n] = value
        return value



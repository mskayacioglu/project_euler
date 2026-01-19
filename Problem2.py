# Even Fibonacci Numbers
# Problem 2
# https://projecteuler.net/problem=2

def even_fibonacci_sum(number):
    a, b = 1, 2
    total = 0
    while a <= number:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total

print(even_fibonacci_sum(4000000))
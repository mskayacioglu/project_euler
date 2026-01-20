# Largest prime factor
# Problem 3
# https://projecteuler.net/problem=3

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def largest_prime_factor(number):
        for i in range(int(number**0.5), 1, -1):
            if number % i == 0 and is_prime(i):
                return i
            
print(largest_prime_factor(600851475143))
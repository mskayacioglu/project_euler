# Largest Palindrome Product
# Problem 4
# https://projecteuler.net/problem=4

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def largest_palindrome_product(min_factor, max_factor):
    largest_palindrome = 0
    for i in range(max_factor, min_factor - 1, -1):
        for j in range(i, min_factor - 1, -1):
            product = i * j
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product
    return largest_palindrome

print(largest_palindrome_product(100, 999))
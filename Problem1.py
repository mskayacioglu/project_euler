# Multiples of 3 or 5
# Problem 1
# https://projecteuler.net/problem=1

number = 1
sum = 0

while number < 1000:
    if number % 3 == 0 or number % 5 == 0:
        sum += number
    number += 1

print(sum)
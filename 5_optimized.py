__author__ = 'Rajat'

'''
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''


def smallest_product(n):
    factors = []

    if n % 2 == 0:
        factors.append(2)

    for y in range(3, n, 2):
        if is_prime(y):
            factors.append(y)

    for x in range(2,n):
        for y in range(2,int(n**0.5)):
            if x**y < n:
                factors.append(x**y)
                if x in factors:
                    factors.remove(x)

    for item1 in factors:
        for item2 in factors:
            if item1 > item2 and item1 % item2 ==0:
                factors.remove(item2)

    smallest_product = 1
    for item in factors:
        smallest_product = smallest_product * item

    return smallest_product


def is_prime(n):
    # This is very slow, need to optimize this
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

print smallest_product(20)

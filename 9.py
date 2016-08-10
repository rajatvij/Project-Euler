import math
__author__ = 'Rajat'

'''
Problem 9
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''


def is_special_pythagorean_triplet(n):
    for a in range(1, n):
        for b in range(1, n):
            c = 1000 - a - b
            if c > b:
                if (a*a + b*b) == c*c:
                    return a*b*c

print(is_special_pythagorean_triplet(1000))

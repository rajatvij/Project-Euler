__author__ = 'Rajat'

'''
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

'''
def is_palindrome(num):
    return str(num) == str(num)[::-1]

maximum = 0
for x in range(1,1000):
    for y in range(1,1000):
        product  = x * y
        if is_palindrome(product) and product > maximum:
            maximum = product

print maximum
'''

# Condensed and optimized version
print(max(x * y for x in range(100, 1000) for y in range(a, 1000) if str(x * y) == str(x * y)[::-1]))

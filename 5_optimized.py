__author__ = 'Rajat'

'''
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''


def smallest_product(n):
    factors = []
    # Check if the number is greater than 2.
    if n > 3:
        factors.append(2)
        # iterate through all odd numbers.
        for y in range(3, n, 2):
            # Check and add prime numbers to the factors.
            if is_prime(y):
                factors.append(y)
        # Check and add all the squares, cubes or other powered numbers 
        # less than the number
        for x in range(2,n):
            # Square root of a number is the largest power 2 can have 
            # which is smaller than number itself.
            for y in range(2,int(n**0.5)):
                if x**y < n:
                    factors.append(x**y)
                    # Check and remove the factors or powered number.
                    if x in factors:
                        factors.remove(x)

        # Check and remove any number is divisible by other number in list.
        for item1 in factors:
            for item2 in factors:
                if item1 > item2 and item1 % item2 ==0:
                    factors.remove(item2)

        smallest_product = 1
        # Get the product of all numbers in list.
        for item in factors:
            smallest_product = smallest_product * item
    
    else:
        return "Please enter a larger number"

    return smallest_product


def is_prime(n):
    # This is very slow, need to optimize this
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            return False
    return True

print smallest_product(20)

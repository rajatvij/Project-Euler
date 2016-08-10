__author__ = 'Rajat'

'''
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''


def get_prime_factors(n):
    results = []

    # iterate over all even numbers first.
    while n % 2 == 0:
        results.append(2)
        n //= 2

    # try odd numbers up to sqrt(n)
    limit = n ** 0.5

    # Starting out with 3, ie., ignoring 1.
    i = 3
    while i <= limit:
        # Checking for divisibility with the ith number and reducing
        # n to reflect the divisibility
        if n % i == 0:
            results.append(i)
            n //= i
        else:
            # Increase i by 2, because the prime numbers are odd except for 2
            i += 2

    return results


def divisible_by_range(num):
    result = 1
    prime_factors = get_prime_factors(num)
    for x in prime_factors:
        result = result * x
    return result

print(divisible_by_range(10))

__author__ = 'Rajat'

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
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

# print(get_prime_factors(13195))

print(max(get_prime_factors(600851475143)))



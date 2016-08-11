__author__ = 'Rajat'

'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


def get_prime_factors(n):
    results = []
    # Check if the number is even.
    if n % 2 == 0:
        results.append(2)
    # Check for all prime factors by iterating through all odd
    # numbers from 3 to square root of number to speed up the process.
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            results.append(x)
            n /= x

    return results

# print(get_prime_factors(13195))

print(max(get_prime_factors(600851475143)))



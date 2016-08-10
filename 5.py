__author__ = 'Rajat'

'''
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
'''


def smallest_divisible(num):
    found = False
    divisible = num
    while not found:
        # note that I'm not increasing by 1, but by the search number itself
        num += divisible
        flag = True
        x = divisible - 1
        # test against all numbers 2..store - 1
        # don't need to test against divisible since we already know it is a
        # factor
        while x > 1:
            if num % x != 0:
                # doesn't divide easily, so break and try next num in sequence
                flag = False
                break
            x -= 1
        if flag:
            return num

# NOTE: I know this can be optimized by looking at multiples of all prime
# numbers under number(20). But this code looks cleaner and i couldn't do
# what i wanted without bloating the code.

print smallest_divisible(10)
print smallest_divisible(20)


#!/usr/bin/python3

'''
Problem 7:

Write a recursive program to determine whether a given integer is prime or not.


Input:
49
999983
1

Output:
not prime
prime
not prime

'''

def is_prime(N, a=3):

    if N == 2:  # special case
        prime = True
    elif N <= 1 or N % 2 == 0:  # too small or even
        prime = False
    elif a * a > N:  # tried all divisors to sqrt, must be prime
        prime = True
    elif (N % a) == 0:  # divides evenly, not a prime
        prime = False
    else:  # can't tell yet, recursively try the next (odd) divisor
        prime = is_prime(N, a+2)

    return prime


if __name__ == '__main__':

	n=int(input())
	a=is_prime(n)

	if a== True:
		print("prime")
	else:
		print("not prime")


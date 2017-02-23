#!/usr/bin/python3


'''
Problem 5:

Write a recursive program to compute n!


Input:
5

Output:
120

'''

def compute_factorial(n):

	if n==1:

		return 1 

	return n*compute_factorial(n-1)


if __name__ == '__main__':
	
	n=int(input())

	print(compute_factorial(n))
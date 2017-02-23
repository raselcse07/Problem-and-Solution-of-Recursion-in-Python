#!/usr/bin/python3

'''
Problem-6:

Write a recursive program to compute nth fibonacci number. 
1st and 2nd fibonacci numbers are 1, 1.

Input:
6

Output:
8

'''

def fib(n):

	if n<3:
		return 1

	return fib(n-1)+fib(n-2)


if __name__ == '__main__':
	
	n=int(input())

	print(fib(n))
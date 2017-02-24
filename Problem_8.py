#!/usr/bin/python3

'''
Problem 8:

Suppose you are given an array of integers in an arbitrary order. 
Write a recursive solution to find the maximum element from the array.


Input:
5
7 4 9 6 2

Output:
9

'''

def maximum_Value(value):

	if len(value) == 1:
		return value[0]
	else:
		return max(value[0],maximum_Value(value[1:]))



n=int(input())
value=[int(x) for x in input().split()]

if n == len(value):
	print(maximum_Value(value))
else:
	print("Out of Range !!")



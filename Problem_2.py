#!/usr/bin/python3

'''
Problem 2:
Write a recursive function to print an array in the following order.

[0] [n-1]
[1] [n-2]
.........
.........
[(n-1)/2] [n/2]

Input:
5
1 5 7 8 9

Output:
1 9
5 8
7 7

'''

def solution(i,j,array):

	if i<=j:

		print("{} {}".format(array[i],array[j]))
		solution(i+1,j-1,array)


if __name__ == '__main__':
	
	n=int(input())
	my_list=[int(x) for x in input().split()]

	if n == len(my_list):

		solution(0,n-1,my_list)
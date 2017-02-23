#!/usr/bin/python3

'''
Problem-9:

Write a recursive solution to find the 
second maximum number from a given set of integers.

Input:
5
5 8 7 9 3

Output:
8

'''

def second_max(_list):

	if len(_list) == 1:

		return _list[0]
	else:
		return max(_list[0],second_max(_list[1:]))


if __name__ == '__main__':

	n=int(input())
	my_list=[int(x) for x in input().split()]
	
	if n == len(my_list):
		
		fmax=second_max(my_list)
		smax=max([x for x in my_list if x != fmax])
		print(smax)

	else:

		print("Array out of range!!!")

 
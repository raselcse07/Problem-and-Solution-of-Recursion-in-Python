#!/usr/bin/python3

'''
Problem-1:

You will be given an array of integers, write a recursive solution to print it in reverse order.

Input:
5
69 87 45 21 47

Output:
47 21 45 87 69

'''

def reverse_list(_list):

	if len(_list) != 1:

		return [_list[-1]]+reverse_list(_list[:-1])
	
	return _list
	

if __name__ == '__main__':
	
	n=int(input())
	my_list=[int(x) for x in input().split()]
	
	if len(my_list) == n:
		result=reverse_list(my_list)
		print(*result)

	else:

		print("Out of range")
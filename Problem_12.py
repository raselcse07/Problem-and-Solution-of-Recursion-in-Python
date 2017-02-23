#!/usr/bin/python3

'''
Problem -12:

Write a recursive solution to get the reverse of a given integer. Function must return an int


Input:
123405

Output:
504321

'''

def reverse_int(numbers):

	if len(numbers) != 1:

		return [numbers[-1]]+reverse_int(numbers[:-1])

	return numbers 


if __name__ == '__main__':
	
	numbers=[int(x) for x in input()]

	result=reverse_int(numbers)
	print(*result,sep='')
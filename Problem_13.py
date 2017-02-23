#!/usr/bin/python3

'''

Probelm-13:

Read a string from keyboard and print it in reversed order. 
You must not use any array to store the characters. 
Write a recursive solutions to solve this problem.

Input:
helloo

Output:
oolleh

'''

def reverse_str(_string):

	if len(_string) != 1:

		return _string[-1]+reverse_str(_string[:-1])

	return _string 

if __name__ == '__main__':

	_string=input()	
	print(reverse_str(_string))
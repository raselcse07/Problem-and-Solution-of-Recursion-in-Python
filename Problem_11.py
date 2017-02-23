#!/usr/bin/python3

'''
Problem-11:

Implement binary search recursively, 
i.e. given an array of sorted integers, find a query integer from it.
Input format: first n, the number of elements. 
Then n integers. Then, q, number of query, then q integers. 
Output format: for each of the q integers, print its index (within 0 to n-1) 
in the array or print 'not found', whichever is appropriate.

Input:
5
1 2 3 4 5
2
3 -5

Output:
2
not found

'''

def binary_Search(array,key):

	if len(array) == 0:

		return False

	mid=len(array)//2

	if array[mid] == key:

		return mid

	else:

		if array[mid] < key :

			return binary_Search(array[mid+1:],key)

		else:

			return binary_Search(array[:mid],key)



if __name__ == '__main__':
	
	n=int(input())
	l=sorted([int(x) for x in input().split()])
	q=int(input())
	key=[int(x) for x in input().split()]

	if n == len(l):

		if q == len(key):

			for i in key:

				index=binary_Search(l,i)

				if index != False:

					print(index)

				else:

					print("not found")
		else:

			print("Key item out of range!!!")

	else:

		print("You can't input more than {}".format(n))








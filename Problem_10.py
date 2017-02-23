#!/usr/bin/python3

'''

Implement linear search recursively, 
i.e. given an array of integers, find a specific value from it.
Input format: first n, the number of elements. 
Then n integers. Then, q, number of query, then q integers. Output format: for each of the q integers, print its index (within 0 to n-1) in the array or print 'not found', whichever is appropriate.


Input:
5
2 9 4 7 6
2
5 9

Output:
not found
1
'''
	

def linear_search(array,key,index=0):

	try:
		if array[index] == key:
			return index

	except IndexError:
		return -1

	return linear_search(array,key,index+1)



if __name__ == '__main__':
	
	n=int(input())
	list_=[int(x) for x in input().split()]
	q=int(input())
	query=[int(x) for x in input().split()]

	if n == len(list_):

		if q == len(query):

			for i in query:
				item=linear_search(list_,i)

				if item != -1:
					print(item)
				else:	
					print("not found")

		else:

			print("Key item out of range!!!")
	else:

		print("You can't input more than {}".format(n))







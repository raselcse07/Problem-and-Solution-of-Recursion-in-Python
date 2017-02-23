#!/usr/bin/python3

'''

Problem 3:

Write a recursive program to remove all odd 
integers from an [1,54,88,6,55,7]. You must not use any extra 
array or print anything in the function. Just read input, call the recursive function, then print the array in main().


Output:
54 88 6

'''

def removeOdd(s,n,i,v,q):

	if s>n:

		return 

	if v[s]%2==0:

		q.append(v[s])

	return removeOdd(s+1,n,i,v,q)

if __name__ == '__main__':
 	
 	v=[1,54,88,6,55,7]
 	q=[]

 
 	removeOdd(0,len(v)-1,0,v,q)

 	for i in range(len(q)):
 		print q[i],




 	


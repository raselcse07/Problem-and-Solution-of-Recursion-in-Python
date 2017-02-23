#!/usr/bin/python3

'''

Problem 4:

Write a recursive solution to print the polynomial series for any input n:
1 + x + x2 + ................. + xn-1


Input:
5

Output:
1 + x + x^2 + x^3 + x^4

'''

def polynomial_series(i,n,a):

	if i<n:
		if i==0:

			a.append("1")
		else:
			a.append("+ x")
			if i>1:
				a.append("^{}".format(i))

		polynomial_series(i+1,n,a)



if __name__ == '__main__':

	a=[]
	n=int(input())
	polynomial_series(0,n,a)

	for i in range(len(a)):
		print(a[i]),

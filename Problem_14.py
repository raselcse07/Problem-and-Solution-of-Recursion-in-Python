#!/usr/bin/python3

'''
Problem-14:

All of you have seen the tower of Hanoi. 
You have 3 pillars 'a', 'b' and 'c', and you need transfer all 
disks from one pillar to another. 

Conditions are, 

only one disk at a time is movable, and you can never place a 
larger disk over a smaller one. 
Write a recursive solution to print the moves that simulates the task,

a -> b means move the topmost of tower a to tower b.

Input:
3

Output:
a -> c
a -> b
c -> b
a -> c
b -> a
b -> c
a -> c

'''

def tower_hanoi(n,start,helper,end):

	if n >= 1:

		tower_hanoi(n-1,start,end,helper)

		print("{} -> {}".format(start,end))

		tower_hanoi(n-1,helper,start,end)


A=["a","b","c"]
start=A[0]
helper=A[1]
end=A[2]

if __name__ == '__main__':

	n=int(input())
	tower_hanoi(n,start,helper,end)



	




# Problem-and-Solution-of-Recursion-in-Python

# Recursions are fun

You may like to try out some simple problems to practice recursions. Try to solve all of them without using any global variables. And try on your own before looking at the solutions. Also please notify any error to me ( rasel_cse07[at]yahoo[dot]com ).

# Problem 1:

You will be given an array of integers, write a recursive solution to print it in reverse order.

'''
    
    Input:
    
    5
    
    69 87 45 21 47
    
    Output:
    
    47 21 45 87 69
'''

# Problem 2:

Write a recursive function to print an array in the following order.
'''

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

# Problem 3:

Write a recursive program to remove all odd integers from an array. You must not use any extra array or print anything in the function. Just read input, call the recursive function, then print the array in main().

'''

    Input:
    6
    1 54 88 6 55 7
    Output:
    54 88 6
'''

# Problem 4:

Write a recursive solution to print the polynomial series for any input n:
1 + x + x2 + ................. + xn-1

'''

    Input:
    5

    Output:
    1 + x + x^2 + x^3 + x^4

'''

# Problem 5:

Write a recursive program to compute n!

'''

    Input:
    5

    Output:
    120
'''


# Problem-6:

Write a recursive program to compute nth fibonacci number. 1st and 2nd fibonacci numbers are 1, 1.

'''

    Input:
    6

    Output:
    8
'''


# Problem 7:

Write a recursive program to determine whether a given integer is prime or not.

'''

    Input:
    49
    999983
    1

    Output:
    not prime
    prime
    not prime
'''


# Problem 8:

Suppose you are given an array of integers in an arbitrary order. Write a recursive solution to find the maximum element from the array.

'''

    Input:
    5
    7 4 9 6 2

    Output:
    9
'''


# Problem-9:

Write a recursive solution to find the second maximum number from a given set of integers.

'''

    Input:
    5
    5 8 7 9 3

    Output:
    8
'''


# Problem-10:

Implement linear search recursively, i.e. given an array of integers, find a specific value from it.Input format: first n, the number of elements. 
Then n integers. Then, q, number of query, then q integers. Output format: for each of the q integers, print its index (within 0 to n-1) in the array or print 'not found', whichever is appropriate.

'''

    Input:
    5
    2 9 4 7 6
    2
    5 9

    Output:
    not found
    1
'''

# Problem-11:

Implement binary search recursively, i.e. given an array of sorted integers, find a query integer from it.Input format: first n, the number of elements. Then n integers. Then, q, number of query, then q integers. Output format: for each of the q integers, print its index (within 0 to n-1) 
in the array or print 'not found', whichever is appropriate.

'''

    Input:
    5
    1 2 3 4 5
    2
    3 -5

    Output:
    2
    not found
'''

# Problem -12:

Write a recursive solution to get the reverse of a given integer. Function must return an int

'''

    Input:
    123405

    Output:
    504321
'''

# Probelm-13:

Read a string from keyboard and print it in reversed order. You must not use any array to store the characters. Write a recursive solutions to solve this problem.

'''

    Input:
    helloo

    Output:
    oolleh
'''

# Problem-14:

All of you have seen the tower of Hanoi. You have 3 pillars 'a', 'b' and 'c', and you need transfer all 
disks from one pillar to another. 

Conditions are, 

only one disk at a time is movable, and you can never place a 
larger disk over a smaller one. 
Write a recursive solution to print the moves that simulates the task,

a -> b means move the topmost of tower a to tower b.

'''

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


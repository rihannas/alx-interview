#!/usr/bin/python3
'''
Create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascals triangle of n:
Returns an empty list if n <= 0
You can assume n will be always an integer
'''
def pascal_triangle(n):
    pascals_triangle = []

    for i in range(n):
        pascals_triangle.append([1]*(i+1))
  
    for i in range(2,n):
        for j in range(1,i):
            pascals_triangle[i][j] = pascals_triangle[i-1][j-1] + pascals_triangle[i-1][j]

    return pascals_triangle
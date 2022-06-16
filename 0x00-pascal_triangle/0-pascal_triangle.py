#!/usr/bin/python3
'''
Create a function def pascal_triangle(n):
that returns a list of lists of integers
representing the Pascals triangle of n:
Returns an empty list if n <= 0
You can assume n will be always an integer
'''


def pascal_triangle(n):
    """
    Return a list of lists, or a null list if n <=0
    """
    triangle = []
    if n <= 0:
        return []
    for x in range(1, n+1):
        if x == 1:
            triangle.append([1])
            continue
        triangle.append(get_floor(triangle[x - 2]))
    return triangle


def get_floor(floor):
    """
    Creates the triangle's floor
    """
    floor_list = [1, 1]
    size = len(floor) - 1

    if size > 0:
        for i in range(size):
            floor_list.insert(i + 1, floor[i] + floor[i + 1])
    return floor_list

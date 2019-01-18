"""
A bubble sort algorithm.
:param a: a list of numbers to sort
"""


def sort(a):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] < a[j]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp

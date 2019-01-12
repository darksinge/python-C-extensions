"""
A bubble sort algorithm written in Cython to speed things up.
"""
cimport cython

# https://cython.readthedocs.io/en/latest/src/tutorial/numpy.html#efficient-indexing
# Setting the boundscheck flag to False improves the efficiency of
# indexing by a considerable amount.
@cython.boundscheck(False)
def sort(int[:] a):

    cdef int arrlen = a.shape[0], i, j, temp

    for i in range(arrlen):
        for j in range(arrlen):

            if a[i] < a[j]:
                temp = a[j]
                a[j] = a[i]
                a[i] = temp

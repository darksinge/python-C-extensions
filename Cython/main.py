import numpy as np
import random
import timeit
import matplotlib.pyplot as plt

import bubble_sort_opt
import bubble_sort


py_proto = """
import random
from __main__ import test_bubble_sort

# seed `random` to get same random numbers for each version of the sorting algo
# random.seed({seed})

test_bubble_sort({size})
"""

c_proto = """
import random
from __main__ import test_bubble_sort_optimized

# seed `random` to get same random numbers for each version of the sorting algo
# random.seed({seed})

test_bubble_sort_optimized({size})
"""


def test_bubble_sort(array_size):
    values = np.array([int(array_size * random.random()) for _ in range(array_size)], dtype=np.int32)
    bubble_sort.sort(values)


def test_bubble_sort_optimized(array_size):
    values = np.array([int(array_size * random.random()) for _ in range(array_size)], dtype=np.int32)
    bubble_sort_opt.sort(values)

def main():
    EXECUTIONS = 10
    REPEAT = 10

    MAX_ARR_SIZE = 2500

    array_sizes = [i for i in range(100, MAX_ARR_SIZE + 1, 100)]
    results = []

    print("Starting speed test.\n")

    for i, size in enumerate(array_sizes):

        # get the formatted strings to use for `timeit`
        #
        # Cython implementation of bubble sort
        c_stmt = c_proto.format(seed=size, size=size)
        # Python implementation of bubble sort
        py_stmt = py_proto.format(seed=size, size=size)

        # use `timeit` to time how long it takes to sort an array of size `size`
        ctimer = timeit.repeat(stmt=c_stmt, repeat=REPEAT, number=EXECUTIONS)
        pytimer = timeit.repeat(stmt=py_stmt, repeat=REPEAT, number=EXECUTIONS)

        # calculate the average time it took to sort an array of random numbers
        ctime = sum(ctimer) / REPEAT
        pytime = sum(pytimer) / REPEAT

        # calculate the ratio of Python execution and Cython execution speed
        t_diff = pytime / ctime

        print("Python took {0:0.3f} seconds to sort {1} elements {2} times.".format(pytime, size, EXECUTIONS))
        print("Cython took {0:0.3f} seconds to sort {1} elements {2} times.".format(ctime, size, EXECUTIONS))
        print("Cython was {:.3f} times faster than Python!".format(t_diff))
        print("==================================================")

        results.append((ctime, pytime, t_diff))

    # get percent increase of cython vs python runtimes
    t_diffs = [result[2] for result in results]

    plt.title('Plot of speed difference between Python\nand Cython code of a bubble sort.')
    plt.xlim(100, MAX_ARR_SIZE)
    plt.ylabel('% Speed Increase\nof Cython code')
    plt.xlabel('Array Size')
    plt.grid(True)
    plt.xlim()

    plt.show()

if __name__ == '__main__':
    main()

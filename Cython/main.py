import sys
import numpy as np
import random
import timeit

import bubble_sort_opt
import bubble_sort

#
# # seed random to get the same random array each time the program is executed
# random.seed(1)

SIZE = 1000
LOOPS = 1000


def test_bubble_sort():
    values = np.array([int(SIZE * random.random()) for _ in range(SIZE)], dtype=np.int32)
    bubble_sort.sort(values)


def test_bubble_sort_optimized():
    values = np.array([int(SIZE * random.random()) for _ in range(SIZE)], dtype=np.int32)
    bubble_sort_opt.sort(values)


if __name__ == '__main__':

    # lenvalues = 100
    # values = np.array([int(lenvalues * random.random()) for _ in range(lenvalues)], dtype=np.int)

    print("Starting bubble sort speed test.\n\tLoops: %d\n\tArray size: %d\n" % (LOOPS, SIZE))

    ctimer = timeit.timeit(test_bubble_sort_optimized, number=LOOPS)
    pytimer = timeit.timeit(test_bubble_sort, number=LOOPS)

    print("Python code took {0:0.2f} seconds to execute {1} times.".format(pytimer, LOOPS))
    print("Cython code took {0:0.2f} seconds to execute {1} times.".format(ctimer, LOOPS))

    print("Cython was {:.2f} times faster than Python!".format(pytimer / ctimer))



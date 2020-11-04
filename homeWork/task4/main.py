
from collections import Counter
import numpy as np


def sort_compare(arr):
    return max([i for i in Counter(arr).values()])


def has_neg(arr):
    return any(i < 0 for i in arr)


def sort_by_unique_values(arr):
    return np.array(sorted(arr, key=sort_compare, reverse=False))


def find_first_neg_row(arr):
    arr_trans = list([list(i) for i in np.array(arr).transpose()])
    return [has_neg(i) for i in arr_trans].index(True)


def main():
    arr = [[0, 0, 2],
           [1, 1, 1],
           [-2, 1, -3]]

    print("Input matrix: \n{}".format(np.array(arr)))
    print("Sorted matrix: \n{}".format(sort_by_unique_values(arr)))
    print("First col with negative element: {}".format(find_first_neg_row(arr)))
    pass


if __name__ == '__main__':
    main()

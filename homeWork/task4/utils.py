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
    out_list = [has_neg(i) for i in arr_trans]
    if True in out_list:
        return out_list.index(True)
    return 'No negative element'

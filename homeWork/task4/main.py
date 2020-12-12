
from utils import *


def main():
    col, rows = int(input('Enter number of columns: ')), int(input('Enter number of rows: '))

    arr = []

    for i in range(rows):
        arr.append([int(i) for i in input().split(' ')])

    print("Input matrix: \n{}".format(np.array(arr)))
    print("Sorted matrix: \n{}".format(sort_by_unique_values(arr)))
    print("First col with negative element: {}".format(find_first_neg_row(arr)))
    pass


if __name__ == '__main__':
    main()

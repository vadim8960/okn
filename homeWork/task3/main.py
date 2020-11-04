import math


def main():
    arr = [3, 2, 1, -5, 4, -6, 7, 5, 9, 8]
    print("Start array: {}".format(arr))
    print("Sum negative elements: {}".format(sum([i if i < 0 else 0 for i in arr])))
    print("Count elements between min and max: {}".format(int(math.fabs(arr.index(max(arr)) - arr.index(min(arr)))) - 1))
    print("Sorted array: {}".format(sorted(arr)))
    pass


if __name__ == '__main__':
    main()

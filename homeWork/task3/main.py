import math


def main():
    size = int(input('Enter size: '))
    print('Enter array: ')
    arr = [int(i) for i in input().split(' ')]
    print("Start array: {}".format(arr))
    print("Sum negative elements: {}".format(sum([i if i < 0 else 0 for i in arr])))
    print("Count elements between min and max: {}".format(int(math.fabs(arr.index(max(arr)) - arr.index(min(arr)))) - 1))
    print("Sorted array: {}".format(sorted(arr)))
    pass


if __name__ == '__main__':
    main()



def main():
    arr = [1, 2, 3, 4, -5, -6, 7, 8, 9, 5]
    print("Sum negative elements: {}".format(sum([i if i < 0 else 0 for i in arr])))

    pass


if __name__ == '__main__':
    main()

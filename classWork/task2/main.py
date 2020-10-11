
if __name__ == '__main__':
    s1 = input('S1: ')
    s2 = input('S2: ')
    n = s1[1::2].rindex(s2)
    print(n)
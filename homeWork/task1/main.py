from math import sqrt, fabs


def pi_from_viet(count_iters):
    res_pi = 1
    up = 0
    for i in range(count_iters):
        up = sqrt(2 + up)
        res_pi *= (up / 2)
    res_pi = 2 / res_pi
    return res_pi


if __name__ == '__main__':
    my_pi = 3.14159265359
    count_iter = 1
    viet_pi = pi_from_viet(count_iter)
    while fabs(my_pi - viet_pi) > 0.00000000001:
        count_iter += 1
        viet_pi = pi_from_viet(count_iter)
        print('Number of iterations: {}. Result: {}.'.format(count_iter, viet_pi))
    print('Result: Pi = {}. Number of iterations: {}.'.format(viet_pi, count_iter))

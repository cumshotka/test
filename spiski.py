import math


def dis(a, b, c):
    return b**2 - 4*a*c


def dis1():
    print('Нет корней')


def dis2(a, b):
    print(-b / 2 * a)


def dis3(b, a, d):
    x1 = (-b + math.sqrt(d)) / 2 * a
    x2 = (-b - math.sqrt(d)) / 2 * a
    print(f'x1 = {round(x1, 3)}', f'x2 = {round(x2, 5)}')


def main(a, b, c):
    d = dis(a, b, c)
    if d > 0:
        dis3(b, a, d)
    elif d == 0:
        dis2(a, b)
    else:
        dis1()


if __name__ ==  '__main__':
    main(1, 4, 2)
import math


def f(x):
    return 3**x - 5*(x**2) + 1

# Ваня
# def f(x):
#     return math.e ** (2*x) + 3*x - 4


def f1(x):
    return math.log(5*x**2 - 1, 3)


# Ваня
# def f1(x):
#     return (math.log(4 - 3*x, math.e))/2


def df(x):
    return 3 * x * math.log(3, math.e) - 10*x


# Ваня
# def df(x):
#     return 2 * math.e ** (2*x) + 3


def phi_dev(x):
    return -3 / (2 * (4 - 3*x))


def dihotomy(a, b, eps):
    counter = 0
    while b-a > eps:
        a1 = a
        b1 = b
        c = (a+b) / 2.0
        if f(b)*f(c) < 0:
            a = c
        else:
            b = c
        print("%d     %.4f     %.4f     %.4f     %.4f     %.4f     %.4f" % (counter, a1, b1, f(a1), f(b1), c, f(c)))
        counter += 1


def newton(a, b, eps):
    counter = 0
    x = b
    t = f(x)/df(x)
    while (math.fabs(t)) > eps:
        print("%d   %.4f   %.4f   %.4f   %.4f " % (counter, x, f(x), df(x), -f(x)/df(x)))
        t = f(x)/df(x)
        x -= t
        counter += 1
    print(x + (-f(x)/df(x)))


def simple_iter(a, b, eps):
    counter = 0
    x = (a+b)/2
    z = f1(x)
    while math.fabs(x-z) >= eps:
        z = x
        x = f1(x)
        print("%d %.4f %.4f" % (counter, z, x))
        counter += 1


print("Метод половинного ділення : ")
dihotomy(0.4, 0.6, 10**-3)
print()
print("---------------")
print("Метод Ньютона : ")
newton(0.4, 0.6, 10**-3)
print()
print("---------------")
print("Метод простої ітерації : ")
simple_iter(0.4, 0.6, 10**-3.5)
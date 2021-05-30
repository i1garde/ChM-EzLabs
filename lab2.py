from math import sin, pi, fabs, sqrt, cos
from numpy import zeros
import numpy as np


# inputed_number = int(input("Введите подпункт, который Вы хотите выбрать : "))


def f(x):
    return (1/x)*sin(pi*x/2)


def rectangle_method(a, b, n=10, eps=1e-4, c=0):
    h = (b-a)/n
    xb = a+c*h
    s = zeros(n)
    print("N-->x-->F-->s-->s1")
    for i in range(n+1):
        x = xb+i*h
        s[i] = s[i-1]+f(x)*h
        print("%d-->%.9f-->%.9f-->%.9f-->%.9f" % (i, x, f(x), s[i], s[i-1]))
        if fabs(s[i-1]-s[i]) < eps:
            break
    return n, s


a = 1.
b = 2.
n = 100
N, S = rectangle_method(a, b, n=1000)
print()


def f(x):
    return sqrt(x)*cos(x)


def trapezoid(f, a, b, Iold, k):
    if k == 1:
        Inew = (f(a) + f(b))*(b - a)/2.0
    else:
        n = 2**(k - 2)  # Кількість нових точок
        h = (b - a)/n  # Крок між точками
        x = a + h/2.0  # Координати першої точки
        summ = 0.0
        for i in range(n):
            summ = summ + f(x)
            x = x + h
            Inew = (Iold + h*summ)/2.0
    return Inew


# Iold = 0.0
# for k in range(1, 21):
#     Inew = trapezoid(f, 0.0, pi, Iold, k)
#     if (k > 1) and (abs(Inew - Iold)) < 10**-6.5:
#         break
#     Iold = Inew
#     print("Інтеграл =", Inew)
#     print("nДілянок =", 2**(k-1))


def n_kr(n):
    while n % 4 != 0:
        n = n + 1
    return n


def method_x():
    eps = 0.001  # Заданная точность
    a = 0  # Нижняя граница интегрирования
    b = 1  # Верхняя граница интегрирования
    # Производим рассчет шага интегрирования
    n_np = round((b - a) / (eps ** (0.25)))
    n = n_kr(n_np)  # Число итераций(округляем до первого числа, кратного четырем)
    h = round((b - a) / n, 3)  # Шаг интегрирования
    # Заполняем массив данных x и f(x)

    x = np.arange(1, 8.01, h).tolist()  # Заполняем список x числами от 1 до 8 с шагом h
    k = 0
    fx = []  # Создаем пустой список значений функции f(x)
    for k in range(0, 1):
        for i in x:
            zn = 1 / (1+i)  # Считаем значение функции f(x) в точках из списка x, функция задается самостоятельно
            fx.append(zn)  # Заполняем список fx значениями функции f(x) в указанных точках


    def integral_1h():
        ih1_s1 = 0  # Вспомогательная переменная, элемент формулы Симпсона
        ih1_s2 = 0  # Вспомогательная переменная, элемент формулы Симпсона

        for i in range(0, 40):
            if i % 2 != 0:
                ih1_s1 += fx[i]  # Суммируем значения функции f(x) в точках с четным номером
            if i % 2 == 0 and i != 40 and i != 0:
                ih1_s2 += fx[i]  # Суммируем значения функции f(x) в точках с нечетным номером

        integral_h1 = h / 3 * (fx[0] + fx[40] + (4 * ih1_s1) + (2 * ih1_s2))  # Считаем интеграл с шагом h
        return integral_h1


    def integral_2h():
        ih2_s1 = 0  # Вспомогательная переменная, элемент формулы Симпсона
        ih2_s2 = 0  # Вспомогательная переменная, элемент формулы Симпсона

        for i in range(2, 39, 4):
            ih2_s1 += fx[i]

        for i in range(4, 37, 4):
            ih2_s2 += fx[i]

        integral_h2 = 2 * h / 3 * (fx[0] + fx[40] + 4 * (ih2_s1) + 2 * (ih2_s2))  # Считаем интеграл с шагом 2h
        return integral_h2


    print('Значение определенного интеграла, посчитаного с шагом h равно', integral_1h())
    print('Значение определенного интеграла, посчитанного с шагом 2h равно', integral_2h())

    Ih_check = abs(integral_1h() - integral_2h()) / 15  # Оценка точности проведенных вычислений методом Ругне-Кутты

    if Ih_check < eps:
        print('Интеграл посчитан верно, точность составила:', Ih_check, ', что выше, чем заданная точность', eps)
    else:
        print('Интеграл посчитан неверно, точность составила:', Ih_check, ', что ниже, чем заданная точность', eps)


method_x()
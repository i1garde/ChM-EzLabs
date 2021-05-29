from math import log, fabs
import numpy as np
from copy import deepcopy
import math


# def System(N, X):
#     if N == 1:
#         return -0.1*X[1]**2-0.2*X[2]**2+0.3
#     elif N == 2:
#         return -0.1*X[1]**2+0.1*X[1]*X[2]+0.7
#
#
# def MPI(n, m, X, eps=1e-3):
#     k = 0
#     while True:
#         d = 0
#         b = deepcopy(X)
#         A = deepcopy(b)
#         A[1] = System(1, X)
#         X[1] = A[1]
#         A[2] = System(2, X)
#         X[2] = A[2]
#         A = deepcopy(b)
#         for i in range(1, n+1):
#             d1 = fabs(X[i]-A[i])
#             if d < d1:
#                 d = d1
#         k += 1
#         if d <= eps:
#             print("Solution is ", X, "\nnumber of iteration =", k)
#             break
#         A = deepcopy(X)
#         if k > m:
#             print("Процес розбігається!")
#             quit()
#
#
# X = np.array([0., 0.25, 0.75])
# n = 2
# m = 10
# MPI(n, m, X)


def jacobian_exercise(x, y):
    return [[1, 2], [2*x, 8*y]]


def function_exercise(x, y):
    return [math.sin(x+y) - 1.6*x, x**2 + y**2 - 1]

####################################################################
'''
def jacobian_exercise(x,y,z):

    return [[1,1,1],[2*x,2*y,2*z],[np.exp(x),x,-x]]

#print (jacobian_exercise(1,2,3))
jotinha  = (jacobian_exercise(1,2,3))

def function_exercise(x,y,z):

    return [x+y+z-3, (x**2)+(y**2)+(z**2)-5,(np.exp(x))+(x*y)-(x*z)-1]

#print (function_exercise(1,2,3))
bezao = (function_exercise(1,2,3))
'''


# def x_delta_by_gauss(J, b):
#     return np.linalg.solve(J, b)


# print(x_delta_by_gauss(jotinha, bezao))
# x_delta_test = x_delta_by_gauss(jotinha, bezao)


# def x_plus_1(x_delta, x_previous):
#     x_next = x_previous + x_delta
#     return x_next


# print (x_plus_1(x_delta_test,[1,2,3]))


def newton_method(x_init):
    first = x_init[0]
    second = x_init[1]
    third = x_init[2]
    jacobian = jacobian_exercise(first, second)
    vector_b_f_output = function_exercise(first, second)
    x_delta = x_delta_by_gauss(jacobian, vector_b_f_output)
    x_plus_1 = x_delta + x_init
    return x_plus_1


def iterative_newton(x_init):
    counter = 0
    x_old = x_init
    print("x_old", x_old)
    x_new = newton_method(x_old)
    print("x_new", x_new)
    diff = np.linalg.norm(x_old-x_new)
    print(diff)
    while diff > 10**-10:
        counter += 1
        print("x_old", x_old)
        x_new = newton_method(x_old)
        print("x_new", x_new)
        diff = np.linalg.norm(x_old-x_new)
        print("diff :", diff)
        x_old = x_new
    convergent_val = x_new
    print("counter :", counter)
    return convergent_val


print(iterative_newton([1, 2]))


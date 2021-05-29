# import numpy as np
# from scipy import interpolate
# from matplotlib import pyplot as plt
#
# x_points = np.array([0, 0.5, 1, 1.5, 2])
# y_points = np.array([0, 0.97943, 1.8415, 2.4975, 2.9093])
#
# # tck : tuple (t,c,k) a tuple containing the vector of knots,
# # the B-spline coefficients, and the degree of the spline.
# tck = interpolate.splrep(x_points, y_points)
#
# for k in range(len(x_points)):
#     print("При", x_points[k], ":", interpolate.splev(x_points[k], tck))
#
# x = np.linspace(0, 2, 100)
# y = interpolate.splev(x, tck)
# plt.plot(x, y)
# plt.show()
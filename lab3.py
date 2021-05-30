import numpy as np


def linear_interp(X, Y, Xp, n=100):
    if (Xp < X[0]) or (Xp > X[n-1]):
        if Xp < X[0]:
            print("Екстраполяція назад")
            i = 1
        if Xp > X[n-1]:
            print("Екстраполяція вперед")
            i = n-1
    else:
        for j in range(1, n):
            if (X[j-1] <= Xp) and (Xp <= X[j]):
                i = j
                j = n
    A = (Y[i]-Y[i-1])/(X[i]-X[i-1])
    B = (Y[i-1]-A*X[i-1])
    Yp = A*Xp+B
    return A, B, Yp


X = np.array([10., 20., 30., 40., 50., 60.])
Y = np.array([0.17365, 0.34202, 0.5, 0.64279, 0.76604, 0.86603])
Xp = 23.

A, B, Yp = linear_interp(X, Y, Xp, n=3)
print("A =", A, "B =", B, "Yp =", Yp)



def LAGR2(X, Y, M, XR, YR, MR):
    """ВХІДНІДАНІ:   X, Y - таблицязначеньфункціїаб
М - довжинатаблиці                      XR - масивробочихточок
MR - кількістьробочихточокВИХІДНІДАНІ:  YR - масивзначеньполіномаЛагранжавробочихточках"""
    def Polynom(X, Y, M, POL):         """підпрограмаформуванняінтерполяційногопо-лінома"""
        POL=np.array(np.zeros(M+1))
        A=np.array(np.zeros(M+1))
        B=np.array(np.zeros(M+1))
        for i in range(1,M+1):
            P=1
            for j in range(1,M+1):
                if j==i: continue
                P=P*(X[i]-X[j])
            P=Y[i]/P
            A[1]=1
            L=1
            for j in xrange(1,M+1):
                if j==i: continue
                C=X[j]
                for k in xrange(1,L+1):
                    B[k+1]=A[k]
                B[1]=0
                for k in xrange(1,L+1):
                    B[k]=B[k]-C*A[k]
                for k in xrange(1,L+2):
                    A[k]=B[k]
                L+=1
            for j in xrange(1,M+1):
                POL[j]=POL[j]+A[j]*P;
        return POL

     def WPOL(POL,M,XR,YR,MR):         """підпрограмаобчисленнязначеньполіномавробочихточках XR[K]"""
        for k in xrange(1,MR+1):
            P=POL[M]
            Z=XR[k]
            for i in xrange(1,M):
                P=POL[M-i]+Z*P
            YR[k]=P
        return YR


POL=np.array(np.zeros(M+1))
POL=Polynom(X,Y,M,POL)
YR=WPOL(POL,M,XR,YR,MR)
return YR
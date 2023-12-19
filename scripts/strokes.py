import sys
import numpy as np

if len(sys.argv) < 2:
    print("Usage: ", sys.argv[0], " N [M = N] [visc = 1]")
else:
    N = int(sys.argv[1])
    M = int(sys.argv[2]) if len(sys.argv) > 2 else N
    mu = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
    Nu = (N + 1) * M
    Nv = N * (M + 1)
    Np = N * M

    Su = 0
    Sv = Nu
    Sp = Nu + Nv
    hx = 1.0 / int(N)
    hx2 = hx * hx
    hy = 1.0 / int(M)
    hy2 = hy * hy
    ia = [0]
    ja = []
    a = []
    b = np.zeros(Nu + Nv + Np)


    def Iu(i, j):
        return Su + (i) * M + (j)


    def Iv(i, j):
        return Sv + (i) * (M + 1) + (j)


    def Ip(i, j):
        return Sp + (i) * M + (j)


    for i in range(N + 1):
        for j in range(M):
            ijpos = len(a)
            bpos = len(ia) - 1

            ja.append(Iu(i, j))
            a.append(0.0)
            if i == 0:
                a[ijpos] = 1.0
                b[bpos] = 1.0
            else:
                ja.append(Iu(i - 1, j))
                a.append(-mu / hx2)
                a[ijpos] += mu / hx2

                if j == 0:
                    a[ijpos] += mu / (0.5 * hy2)
                else:
                    ja.append(Iu(i, j - 1))
                    a.append(-mu / hy2)
                    a[ijpos] += mu / hy2

                if j == M - 1:
                    a[ijpos] += mu / (0.5 * hy2)
                else:
                    ja.append(Iu(i, j + 1))
                    a.append(-mu / hy2)
                    a[ijpos] += mu / hy2

                if i < N:
                    ja.append(Iu(i + 1, j))
                    a.append(-mu / hx2)
                    a[ijpos] += mu / hx2
                if i == N:
                    ja.append(Ip(i - 1, j))
                    a.append(-1.0 / (0.5 * hx))
                else:
                    ja.append(Ip(i - 1, j))
                    a.append(-1.0 / hx)

                    ja.append(Ip(i, j))
                    a.append(1.0 / hx)
            ia.append(len(ja))

    for i in range(N):
        for j in range(M + 1):
            ijpos = len(a)
            bpos = len(ia) - 1

            ja.append(Iv(i, j))
            a.append(0.0)
            if j == 0 or j == M:
                a[ijpos] = 1.0
                b[bpos] = 0.0
            else:
                if i == 0:
                    a[ijpos] += mu / (0.5 * hx2)
                else:
                    ja.append(Iv(i - 1, j))
                    a.append(-mu / hx2)
                    a[ijpos] += mu / hx2

                ja.append(Iv(i, j - 1))
                a.append(-mu / hy2)
                a[ijpos] += mu / hy2

                ja.append(Iv(i, j + 1))
                a.append(-mu / hy2)
                a[ijpos] += mu / hy2

                if i < N - 1:
                    ja.append(Iv(i + 1, j))
                    a.append(-mu / hx2)
                    a[ijpos] += mu / hx2

                ja.append(Ip(i, j))
                a.append(1.0 / hy)

                ja.append(Ip(i, j - 1))
                a.append(-1.0 / hy)
            ia.append(len(ja))

    for i in range(N):
        for j in range(M):
            ijpos = len(a)
            bpos = len(ia) - 1

            ja.append(Ip(i, j))
            a.append(0.0)
            b[bpos] = 0.0

            ja.append(Iu(i, j))
            a.append(-1.0 / hx)
            ja.append(Iu(i + 1, j))
            a.append(1.0 / hx)

            ja.append(Iv(i, j))
            a.append(-1.0 / hy)
            ja.append(Iv(i, j + 1))
            a.append(1.0 / hy)
            ia.append(len(ja))

    with open("A.mtx", "w") as output, open("b.txt", "w") as vec:
        output.write("%%MatrixMarket matrix coordinate real general\n")
        output.write(str(len(ia) - 1) + " " + str(len(ia) - 1) + " " + str(len(ja)) + "\n")
        vec.write(str(len(ia) - 1) + "\n")

        for i in range(len(ia) - 1):
            for j in range(ia[i], ia[i + 1]):
                output.write(str(i + 1) + " " + str(ja[j] + 1) + " " + str(a[j]) + "\n")
            vec.write(str(b[i]) + "\n")



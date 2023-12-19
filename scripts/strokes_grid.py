import sys
import numpy as np


def main(argv):
    argc = len(argv)
    print(argc, "аргументы")
    if argc < 3:
        print("Usage:", argv[0], "x.txt N [M = N]")
    else:
        file = argv[1]
        N = int(argv[2])
        M = int(argv[3]) if argc > 3 else N
        Nu = (N + 1) * M
        Nv = N * (M + 1)
        Np = N * M

        Su = 0
        Sv = Nu
        Sp = Nu + Nv
        hx = 1.0 / N
        hy = 1.0 / M
        x = []

        def Iu(i, j):
            return Su + i * M + j

        def Iv(i, j):
            return Sv + i * (M + 1) + j

        def Ip(i, j):
            return Sp + i * M + j

        with open(file, 'r') as inp:
            Nt = float(inp.readline())
            print(Nt, "Nt")
            print(Nu, "Nu")
            print(Nv, "Nv")
            print(Np, "Np")
            if Nt != Nu + Nv + Np:
                print("incorrect size!")
                return -1
            for k in range(int(Nt)):
                x.append(float(inp.readline()))

        with open("grid_python.vtk", 'w') as outp:
            outp.write("# vtk DataFile Version 2.0\n")
            outp.write("Results\n")
            outp.write("ASCII\n")
            outp.write("DATASET STRUCTURED_POINTS\n")
            outp.write("DIMENSIONS {} {} {}\n".format(N, M, 1))
            outp.write("ORIGIN 0 0 0\n")
            outp.write("SPACING {} {} {}\n".format(hx, hy, 1))
            outp.write("POINT_DATA {}\n".format(N * M))
            outp.write("SCALARS PRESSURE double\n")
            outp.write("LOOKUP_TABLE default\n")
            for j in range(M):
                for i in range(N):
                    outp.write("{}\n".format(x[Ip(i, j)]))
            outp.write("SCALARS VELOCITY double 3\n")
            outp.write("LOOKUP_TABLE default\n")
            for j in range(M):
                for i in range(N):
                    outp.write("{} {} {}\n".format((x[Iu(i + 1, j)] + x[Iu(i, j)]) * 0.5,
                                                   (x[Iv(i, j + 1)] + x[Iv(i, j)]) * 0.5, 0.0))
            outp.write("SCALARS DIVERGENCE double\n")
            outp.write("LOOKUP_TABLE default\n")
            for j in range(M):
                for i in range(N):
                    outp.write(
                        "{}\n".format((x[Iu(i + 1, j)] - x[Iu(i, j)]) / hx + (x[Iv(i, j + 1)] - x[Iv(i, j)]) / hy))

    return 0


if __name__ == "__main__":
    main(sys.argv)



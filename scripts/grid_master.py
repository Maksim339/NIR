import sys
import numpy as np


def paraview(argv):
    argc = len(argv)
    if argc < 2:
        print("Usage:", argv[0], "spe_phi.dat")
    else:
        file = argv[1]
        phi_data = np.loadtxt(file).reshape((60, 220, 85), order='F')

        with open("spe_phi.vtk", 'w') as outp:
            outp.write("# vtk DataFile Version 2.0\n")
            outp.write("Porosity Data\n")
            outp.write("ASCII\n")
            outp.write("DATASET STRUCTURED_POINTS\n")
            outp.write("DIMENSIONS 60 220 85\n")
            outp.write("ORIGIN 0 0 0\n")
            outp.write("SPACING 1 1 1\n")
            outp.write("POINT_DATA {}\n".format(60 * 220 * 85))

            outp.write("SCALARS PorosityX double 1\n")
            outp.write("LOOKUP_TABLE default\n")
            for k in range(85):
                for j in range(220):
                    for i in range(60):
                        outp.write("{}\n".format(phi_data[i, j, k]))


if __name__ == "__main__":
    paraview(sys.argv)

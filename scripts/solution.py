from scipy.io import mmread
import sys
import numpy as np
import scipy.sparse.linalg


# Пути по умолчанию
default_path_to_A_mtx = 'A.mtx'
default_path_to_b_txt = 'b.txt'

path_to_A_mtx = sys.argv[1] if len(sys.argv) > 1 else default_path_to_A_mtx
path_to_b_txt = sys.argv[2] if len(sys.argv) > 2 else default_path_to_b_txt

A = mmread(path_to_A_mtx).tocsc()
b = np.loadtxt(path_to_b_txt)

b_corrected = b[1:]

solution = scipy.sparse.linalg.spsolve(A, b_corrected)

solution_with_length = np.insert(solution, 0, len(solution))

np.savetxt('solution.txt', solution_with_length, fmt='%f')

from scipy.io import mmread
import numpy as np
import scipy.sparse.linalg

path_to_A_mtx = 'A.mtx'
path_to_b_txt = 'b.txt'  

A = mmread(path_to_A_mtx).tocsc()

b = np.loadtxt(path_to_b_txt)

b_corrected = b[1:]

solution = scipy.sparse.linalg.spsolve(A, b_corrected)

np.savetxt('solution.txt', solution)


import numpy as np
cimport numpy as np
import cython
from cython.parallel import prange, parallel

DTYPE = np.double
ctypedef np.double_t DTYPE_t

# C = A * B
@cython.boundscheck(False)
def mydgemm(np.ndarray[DTYPE_t, ndim=2] A, np.ndarray[DTYPE_t, ndim=2] B):
    assert A.dtype == DTYPE and B.dtype == DTYPE
    assert A.shape[1] == B.shape[0]

    cdef int imax = A.shape[0]
    cdef int kmax = A.shape[1]
    cdef int jmax = B.shape[1]
    cdef int i, j, k
    cdef np.ndarray[DTYPE_t, ndim=2] C = np.zeros([imax, jmax], dtype=DTYPE, order='C')
    
    with nogil, parallel():
        for i in prange(imax, schedule="static"):
            for k in range(kmax):
                for j in range(jmax):
                    C[i, j] += A[i, k] * B[k, j]

    return C
                    

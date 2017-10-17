#!/usr/bin/env python3

import numpy as np

def mydgemm2(A, B):
    assert A.shape[1] == B.shape[0]
    imax = A.shape[0]
    kmax = A.shape[1]
    jmax = B.shape[1]
    C = np.zeros((imax, jmax), dtype=np.float64)

    for i in range(imax):
        for k in range(kmax):
            for j in range(jmax):
                C[i, j] += A[i, k] * B[k, j]

    return C

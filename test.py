#!/usr/bin/env python3

import os, sys
import numpy as np
from numpy.random import *
import mydgemm as md
from mydgemm2 import *
import time as T

def main():
    argv = sys.argv
    argc = len(argv)
    s = 7777
    seed(s)
    if argc == 1:
        size = 128
    else:
        size = int(argv[1])
    C = np.zeros((size, size), dtype=np.float64)
    A = np.array(rand(size, size), dtype=np.float64)
    B = np.array(rand(size, size), dtype=np.float64)

    print("matrix size:", size, "x", size)
    
    t0 = T.time()
    C = md.mydgemm(A, B)
    time = T.time() - t0
    np.save("mydgemm.out", C)
    print("time for mydgemm()[s]:", time)
    
    C = 0.0
    t0 = T.time()
    C = mydgemm2(A, B)
    time = T.time() - t0
    np.save("mydgemm2.out", C)
    print("time for mydgemm2()[s]:", time)

    C = 0.0
    t0 = T.time()
    C = np.dot(A, B)
    time = T.time() - t0
    np.save("np.dot.out", C)
    print("time for np.dot()[s]:", time)
    
if __name__ == "__main__":
    main()

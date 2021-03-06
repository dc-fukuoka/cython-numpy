openmp-python - matrix-matrix multiplication with cython + numpy and OpenMP.
====
intel compiler is required.  
how to run:
~~~
$ vi setup.py # <--- rewrite library_dirs if needed
$ python setup.py build
$ cp -p build/lib.linux-x86_64-3.6/mydgemm.cpython-36m-x86_64-linux-gnu.so .
$ ./test.py <size of matrices>
~~~
performance comparison between cython+numpy version, numpy+normal loop version and numpy.dot() version (with intel xeon E5-2680, 16 cores):
~~~
$ ./test.py 256
matrix size: 256 x 256
time of mydgemm()[s]: 0.02587437629699707
time of mydgemm2()[s]: 13.816595792770386 # this is made by normal python for loop, too slow
time of np.dot()[s]: 0.009705066680908203
$ cmp mydgemm.out.npy np.dot.out.npy
$ cmp mydgemm.out.npy mydgemm2.out.npy # <-- there is no difference between the results
~~~

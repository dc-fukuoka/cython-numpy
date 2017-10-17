cython+numpy - matrix-matrix mutiplication with cython + numpy and OpenMP.
====
how to run:
~~~
$ python setup.py build
$ cp -p build/lib.linux-x86_64-3.6/mydgemm.cpython-36m-x86_64-linux-gnu.so .
$ ./test.py <size of matrices>
~~~
performance comparison (with intel xeon E5-2680):
~~~
$ ./test.py 256
matrix size: 256 x 256
time of mydgemm()[s]: 0.02587437629699707
time of mydgemm2()[s]: 13.816595792770386 # this is made by normal python for loop, too slow
time of np.dot()[s]: 0.009705066680908203
~~~

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension("mydgemm", ["mydgemm.pyx"],
                         library_dirs=['/opt/intel/compilers_and_libraries_2018.0.128/linux/compiler/lib/intel64/'],
                         libraries=['irc'],
                         extra_compile_args=['-qopenmp'],
                         extra_link_args=['-liomp5'])]

setup(
  name = 'mydgemm',
  cmdclass = {'build_ext': build_ext},
  ext_modules = ext_modules
)

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import build_ext
import numpy

setup(
      name="Merge sort program",
      ext_modules=[
            Extension('bubble_sort_opt',
                      sources=['bubble_sort_opt.pyx'],
                      extra_compile_args=['-O3'],
                      language='c++')
      ],
      include_dirs=[numpy.get_include()],
      cmdclass={'build_ext': build_ext}
)

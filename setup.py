import os
from setuptools import setup
import sys

sys.path.append('/home/w/.local/lib/python3.8/site-packages')


from torch.utils.cpp_extension import CppExtension, BuildExtension

# Python interface
setup(
    name='arcsim',
    install_requires=['torch'],
    ext_modules=[
        CppExtension(
            name='arcsim',
            include_dirs=['./arcsim/src/','./arcsim/dependencies/include'],
            sources=[
                'pybind/bind.cpp',
            ],
            libraries=['make_pytorch','json','taucs','alglib',
            'png','z','lapack','blas','boost_system','boost_filesystem','boost_thread','gomp','glut','GLU','GL','glapi','GLdispatch'],
            library_dirs=['objs','./arcsim/dependencies/lib','/usr/lib/x86_64-linux-gnu/'],
        )
    ],
    cmdclass={'build_ext': BuildExtension},
    zip_safe=False,
)

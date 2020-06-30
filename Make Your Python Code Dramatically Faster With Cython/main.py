'''
Make Your Python Code Dramatically Faster With Cython

Installing Cython
pip install Cython

Compile the code
python setup.py build_ext --inplace
'''

import run_python
import run_cython
from timeit import timeit


cythonTime = timeit('run_cython.fastfactorial(20)', globals=globals(), number=100000)
pythonTime = timeit('run_python.factorial(20)', globals=globals(), number=100000)
print(f"Cython: {cythonTime}")
print(f"Python: {pythonTime}")
print(f"Cython is {pythonTime//cythonTime} times faster than python")
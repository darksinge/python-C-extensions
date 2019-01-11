from distutils.core import setup, Extension

hellomodule = Extension('hello',
                        sources=['hellomodule.cpp'])

setup(name="hello",
      version='0.1',
      description='This is a demo package',
      ext_modules=[hellomodule])


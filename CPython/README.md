# CPython "hello.py" example

This folder contains an example of using the Python/C API to create an extension in C++ for Python 3.6.

This conatins a trivial example in `hellomodule.cpp` that creates a Python module called `hello`, 
and contains a method named `hello` (I tried to be as original as I could). Although the
code is written entirely in C++, the module may be invoked in Python by calling `hello.hello('your name')`, 
which then returns a simple "hello" message.

## dependencies

This project was created on a Debian based Linux distribution. I do not guarentee this will work on Windows.

The python-dev package must be installed to obtain the `Python.h` header file needed to build the extension.
You'll also need a C and C++ compiler, and cmake if not already installed on your system. 

```bash
sudo apt install python3-dev gcc g++ cmake
``` 

## building

From inside the directory of the project (`python-C-extensions/CPython/`):
```bash
python setup.py build
python setup.py install
```
This should install a new Python module called `hello` in your Python's `site-packages` folder.

## running

You can either run `main.py` directly, or use the new `hello` module inside the Python REPL.

```
>>> import hello
>>> result = hello.hello("Mr. Anderson")
>>> print(result)
Hello, Mr. Anderson.
```


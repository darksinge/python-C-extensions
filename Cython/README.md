# Cython Examples

This code was tested using Python 3.6 and 3.7. Basically, Cython can be used
to make your Python code speedy fast.

## Installation

Python version: 3.6 or 3.7

Install required packages.
```bash
pip install numpy matplotlib cython
```

If running this on Debian based Linux distribution, you might need to install
Tkinter, which is a dependency of matplotlib.
```bash
sudo apt install python3-tk
```

## Building

From inside `Cython/`, run the following command:

```bash
python setup.py build_ext --inplace
```

## Running

Run `python main.py` from inside of a terminal.

#include <python3.6/Python.h>
#include <string>
#include <iostream>

std::string hello(char * name)
{
    std::string result = "Hello, " + std::string(name) + ".";
    return result;
}

static PyObject *hello_wrapper(PyObject *self, PyObject *args)
{
    PyObject *pyName;

    // parse arguments
    if (!PyArg_ParseTuple(args, "U:hello", &pyName)) {
        return NULL;
    }

    // convert PyObject to char *
    PyObject *namestr = PyUnicode_AsEncodedString(pyName, "utf-8", "~E~");
    char *name = PyBytes_AS_STRING(namestr);

    // call the custom `hello` function
    std::string message = hello(name);

    // build the result and return a valid Python object
    PyObject *result = Py_BuildValue("U", message.c_str());
    return result;
}

static PyMethodDef HelloMethods[] = {
        { "hello", hello_wrapper, METH_VARARGS, "A simple hello function" },
        { NULL, NULL, 0, NULL }
};

static struct PyModuleDef hellomodule = {
        PyModuleDef_HEAD_INIT,
        "hello", /* name of the module */
        NULL,    /* module docs, may be NULL */
        -1,      /* size of per-interpreter state of the module, or -1 if the module keeps state in global variables */
        HelloMethods
};

PyMODINIT_FUNC PyInit_hello(void)
{
    return PyModule_Create(&hellomodule);
}


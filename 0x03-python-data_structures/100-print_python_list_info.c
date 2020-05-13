#include <Python.h>
/**
 * print_python_list_info - print some basic info about Python lists
 * @p: PyObject
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
long int i, size;
size = Py_SIZE(p);
PyObject *n;

printf("[*] Size of the Python List = %li\n", size);
printf("[*] Allocated = %li\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
n = PyList_GetItem(p, i);
printf("Element %ld: %s\n", i, Py_TYPE(n)->tp_name);
}
}

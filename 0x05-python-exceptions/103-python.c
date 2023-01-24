#include "Python.h"
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>

PyAPI_FUNC(void) print_python_bytes(PyObject * p);
PyAPI_FUNC(void) print_python_list(PyObject * p);

/**
 * print_python_bytes - print some basic info about Python lists
 * @p: A PyObject
 *
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t i, k, sz;
	char *s;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	sz = PyBytes_Size(p);
	s = ((PyBytesObject *)p)->ob_sval;
	printf("  size: %ld\n", sz);
	printf("  trying string: ");
	for (i = 0, k = 0; i < sz; i++)
	{
		printf("%c", s[k]);
		if (!isprint(s[k++]))
			break;
	}
	printf("\n");
	sz += 1;
	sz = sz > 10 ? 10 : sz;
	printf("  first %ld bytes:", sz);
	for (i = 0, k = 0; i < sz; i++)
		printf(" %02x", (unsigned char)s[k++]);
	printf("\n");
}

/**
* print_python_float - print python float object
* @p: A PyObject
*
* Return: void
*/
void print_python_float(PyObject *p)
{

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	printf("  value: ");
	PyObject_Print(p, stdout, 0);
	printf("\n");
}
/**
 * print_python_list - print python list
 * @p: A PyObject
 *
 * Return: void
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t len;
	Py_ssize_t i = 0;
	PyObject *tmp;

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	len = ((PyVarObject *)p)->ob_size;

	printf("[*] Size of the Python List = %ld\n", len);
	printf("[*] Allocated = %ld\n", ((PyListObject *) p)->allocated);
	for (i = 0; i < len; i++)
	{
		tmp = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, tmp->ob_type->tp_name);
		if (PyBytes_Check(tmp))
			print_python_bytes(tmp);
		else if (PyFloat_Check(tmp))
			print_python_float(tmp);
	}
}

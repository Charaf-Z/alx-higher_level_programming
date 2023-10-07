#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Print information about a Python list
 * @p: A pointer to the Python list to print information about
 */
void print_python_list_info(PyObject *p)
{
	int size = Py_SIZE(p);
	int idx = 0;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", ((PyListObject *)p)->allocated);

	for (; idx < size; idx++)
		printf("Element %d: %s\n",
		idx, Py_TYPE(((PyListObject *)p)->ob_item[idx])->tp_name);
}

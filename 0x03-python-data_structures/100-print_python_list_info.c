#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - Print information about a Python list
 * @p: A pointer to the Python list to print information about
 */
void print_python_list_info(PyObject *p)
{
	size_t size, alloc;
	int idx;
	PyObject *object;

	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", alloc);

	for (; idx < size; ++idx)
	{
		printf("Element %d: ", idx);
		object = PyList_GetItem(p, idx);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}

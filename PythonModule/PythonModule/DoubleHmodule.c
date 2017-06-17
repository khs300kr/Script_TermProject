#include <python.h>
#include <io.h>

static PyObject *
DoubleH_CountCurrentFile(PyObject *self, PyObject *args)
{
	int id = 0;
	int retval = 0;

	char* path;
	if (!PyArg_ParseTuple(args, "s", &path))
		return NULL;

	while (1) {
		char str[256];
		sprintf(str, "%s\\%d.jpg", path, id);

		int retval = access(str, 0);
		if (retval == 0) {
			id += 1;
			continue;
		}
		else if (retval == -1) {
			return Py_BuildValue("i", id);
		}
	}
}

static PyMethodDef DoubleHMethods[] = {
	{ "CountCurrentFile", DoubleH_CountCurrentFile, METH_VARARGS, "Count the current file" },
	{ NULL, NULL, 0, NULL }
};

static struct PyModuleDef DoubleHmodule = {
	PyModuleDef_HEAD_INIT,
	"DoubleH",
	"It is DoubleH module.",
	-1, DoubleHMethods
};
PyMODINIT_FUNC
PyInit_DoubleH(void)
{
	return PyModule_Create(&DoubleHmodule);
}
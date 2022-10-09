import ctypes

class CreateArray:
    # Creates an array with size elements
    def __init__(self, size):
        self._size = size

        PyArrayType = ctypes.py_object * size
        self._elements = PyArrayType()

    # Get the contents of the index element
    def __getitem__(self, index):
        return self._elements[index]

    # Put the value in the array elements at index position
    def __setitem__(self, index, value):
        self._elements[index] = value

    # Array Iterator
    def __iter__(self):
        return _ArrayIterator(self._elements)


# Iterator for the array ADT
class _ArrayIterator:
    def __init__(self, theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._curNdx]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration
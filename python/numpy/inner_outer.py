import numpy
A, B = numpy.array([input().split() for _ in range(2)],int)
print(numpy.inner(A, B))
print(numpy.outer(A, B))
cimport numpy
n, m = map(int, input().split())
A = numpy.array([input().split() for _ in range(n)],int)
print(numpy.transpose(A))
print(A.flatten())
from collections import namedtuple
n, student = int(input()), namedtuple('Student', input().split())
print(sum(map(int,[[x for x in input().split()][student._fields.index('MARKS')] for _ in range(n)]))/n)
import numpy as np
import itertools
import math
from sympy import Line, Point
p = np.random.rand(4,2)
def rst(p, q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)
pp = list(itertools.combinations(p,2))
for i in pp:
    rs = rst(i[0], i[1])
    print(rs)
for i in pp:

    p1, p2 = Point(i[0]), Point(i[1])
    #print(p1, p2)
    l1 = p1.distance(p2)
    print(l1.evalf(), 'sym')

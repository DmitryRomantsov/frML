import numpy as np
import itertools
import math
import matplotlib.pyplot as plt
from sympy import Line, Point
p = np.random.rand(5,2)
def rst(p, q):
    return math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)
pp = list(itertools.combinations(p,2))
#ferst metod
for i in pp:
    rs = rst(i[0], i[1])
    print(rs)
#second metod
for i in pp:

    p1, p2 = Point(i[0]), Point(i[1])
    #print(p1, p2)
    l1 = p1.distance(p2)
    print(l1.evalf(), 'sym')
#... 3
for i in pp:
    di = np.linalg.norm(i[0]-i[1])
    dy = (i[0][1] + i[1][1])/2
    dx = (i[1][0] + i[0][0])/2
    plt.text(dx, dy, str(di))
    plt.plot((i[0][0], i[1][0]),(i[0][1],i[1][1]))
plt.show()
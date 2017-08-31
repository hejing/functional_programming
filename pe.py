import itertools
from random import random

from pipe import *

# pipeline expression.  f = g()

print range(5) | add
print range(10) | where(lambda x: x%2==0) | take(3) | as_list
# select == map
print itertools.count(1) | take(5) | aggregate(lambda pos,_: pos | select(lambda x:x+1 if ramdon()>0.3 else x), initializer=[1,1,1]) | as_list

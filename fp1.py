from random import random

# times=5
# positions=[1,1,1]

# while times > 0:
#     times -= 1

#     print ''
#     for i in range(len(positions)):
#         if random() > 0.3:
#             positions[i] += 1
#         print '-' * positions[i]

print reduce(lambda pos,_:map(lambda x: (x+1) if random()>0.3 else x, pos),range(5), [1,1,1])

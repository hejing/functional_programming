

# arr = [1,2,3,4,5]
# arr = range(5)

# def my_sum(numbers):
#     total = 0
#     for i in numbers:
#         total = total + i
#     return total

# print my_sum(arr)

# def my_product(numbers):
#     total = 1
#     for i in numbers:
#         total = total * i
#     return total
#     return totaltotal

# print my_product(arr)

# def my_reduce(numbers, fn, initial):
#     total = initial
#     for i in numbers:
#         total = fn(total, i)
#     return total


# print my_reduce(arr, lambda t,x: t+x, 0)
# print my_reduce(arr, lambda t,x: t*x, 1)

# print all([True, True, True])
# print any([False, False, True])
# print sum(arr)
# print max(arr)
# print min(arr)

# # map fn with iterator
# print map(lambda x: x+10, arr)
# # filter list out of iterator
# print filter(lambda x: x%2==0, arr)

# print arr
# lst = range(10, 20)
# lst1 = range(5,15)
# # zip combine multiple lists to 1
# print zip(arr, lst, lst1)

# # sorted a list by key
# print sorted([74,56,23,105], key=lambda x:x)

# def f(a):
#     print a

# print reduce(lambda _,x: f(x), range(5), 0)

# 3辆车比赛， 分别给3辆车70%的概率往前走一步，一共有5次机会，我们打出每次这3辆车的前行状态

from random import random

times=5
positions=[1,1,1]

while times > 0:
    times -= 1

    print ''
    for i in range(len(positions)):
        if random() > 0.3:
            positions[i] += 1
        print '-' * positions[i]

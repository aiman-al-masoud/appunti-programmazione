from functools import reduce

def my_sum(*args):
    return reduce(lambda x,y:x+y, args)

my_sum(1,2,3,4) # 10

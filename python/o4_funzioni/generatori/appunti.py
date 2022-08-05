def gen():
    x = 0
    while True:
        yield x
        x+=1

i = gen() 
next(i)

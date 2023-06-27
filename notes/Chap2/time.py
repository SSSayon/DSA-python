import time, timeit

def f1():
    pass

def f2():
    lst = list(range(1000))

start = time.time()

t1 = timeit.Timer("f1()", "from __main__ import f1")
print(t1.timeit(number=100000))
t2 = timeit.Timer("f2()", "from __main__ import f2")
print(t2.timeit(number=100000))

end = time.time()

print(end - start)

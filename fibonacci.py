def fib():
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b
for f in fib():
    if f > 41:
        break
    print(f)
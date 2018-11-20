def fib(max=10):
    a = 1
    b = 2
    while a < max:
        yield a
        a, b = b, a+b


print(sum([i for i in fib(4000000) if i % 2 == 0]))

def fib(n):
    f = [1, 2]
    while (f[-1]+f[-2] < n):
        f.append(f[-1] + f[-2])
    return f

print(sum([i for i in fib(4000000) if i % 2==0]))

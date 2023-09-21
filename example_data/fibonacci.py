def fib(n):
    if n < 2:
        return n
    else:
        # fn = fn-1 + fn-2
        return fib(n-1) + fib(n-2)

fibonacci = []
for x in range(10):
    fibonacci.append(fib(x))

print(fibonacci)
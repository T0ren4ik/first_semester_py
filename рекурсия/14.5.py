def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-2) + fib(n-1)


n = 10
for i in range(n+1):
    print(f'f{i} = {fib(i)}')
print()

k = 10
m = 13

i = 0
while fib(i) <= m:
    i += 1

print(f'Первый член последовательности больший {m}: f{i} == {fib(i)}')

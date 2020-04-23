from math import factorial
n = int(input())
a = [int(i) for i in range(1, 15)]
def fibo_gen(n):
    for i in a:
        yield factorial(n)

for i in fibo_gen(n):
    print(i)






from functools import reduce
a = [i for i in range(99, 1001) if i % 2 == 0]
print(a)

def my_func(prev_i, i):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_i * i

print(reduce(my_func, a))


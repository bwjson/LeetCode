def my_generator(n):
    for i in range(n + 1):
        yield i

gen = my_generator(5)
for i in gen:
    print(i, end=" ")

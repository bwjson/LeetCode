numbers = []

def append_decorator(arg):
    def actual_decorator(foo):
        def wrapper(*args, **kwargs):
            for i in range(arg):
                foo(*args, **kwargs)
        return wrapper
    return actual_decorator

@append_decorator(3)
def append(n):
    numbers.append(n)
    

append(3)
print(numbers)


    

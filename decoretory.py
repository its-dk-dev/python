import time


def cache(func):
    """
    This cache decoretor will cache the last execution result in a memory.
    If function called with the same input data as earlier again,
    then it will return cache data
    """
    cache = {}
    def wrapper(*args, **kwargs):
        if args not in cache:
            result = func(*args, **kwargs)
            cache[args] = result
        return cache[args]
    
    return wrapper

def debug(func):
    """
    This debug decoretor will debug the function
    and print the details
    """
    def wrapper(*args, **kwargs):
        print("Debugger attached")
        print(f"{func.__name__} function having '{', '.join(args)}' as a paramters")
        return func(*args, **kwargs)
    
    return wrapper

@debug
def greet(*args, **kwargs):
    message = "Good Morning, Have a great day"
    for key, value in kwargs.items():
        if key == "greeting":
            message = value
    print(f"{message} {args[0]}")

# greet("John", "Samsung", greeting= "Have a great day")

@cache
def heavy_operation(a, b):
    print("Operation Started")
    time.sleep(5)
    print("Operation completed successfully")
    return a ** b

print(heavy_operation(2, 3))
print(heavy_operation(2, 3))
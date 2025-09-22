from functools import wraps

def decorated(level=None):
    print(f"You chose the level: {level}")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Running {func.__name__}")
            result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

def plain_function():
    print("Nothing to see here")


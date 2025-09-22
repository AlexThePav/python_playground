from utils import decorated, plain_function


decorated_result = decorated()
print(decorated_result)


@decorated(level="Boss")
def say_hello(name=None):
    return f"Hello {name}"


if __name__ == "__main__":
    result = say_hello("My little friend")
    print(result)

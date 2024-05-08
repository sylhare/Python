def handle_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error: {e}")
            return None

    return wrapper


def hello(message):
    """ creates a decorator that adds a message to the return value of the decorated function"""

    def hello_decorator(func):
        def wrapper(*args, **kwargs):
            return f"hello {func(*args, **kwargs)}: {message}"

        return wrapper

    return hello_decorator


def decorator(func):
    def wrapper(arg: str) -> str:
        return "decorated " + func(arg)

    return wrapper

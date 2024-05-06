def decorator1(func):
    def wrapper1(*args, **kwargs):
        print('Decorator 1 before function call')
        result = func(*args, **kwargs)
        print('Decorator 1 after function call')
        return result

    return wrapper1


def decorator2(func):
    def wrapper2(*args, **kwargs):
        print('Decorator 2 before function call')
        result = func(*args, **kwargs)
        print('Decorator 2 after function call')
        return result

    return wrapper2


@decorator1
@decorator2
def hello():
    print('Hello world')


if __name__ == "__main__":
    hello()

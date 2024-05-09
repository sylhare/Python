from src.examples.snippet.src.decorator import handle_error, hello, decorator, decorator_maker


def test_handle_error_decorator():
    @handle_error
    def example():
        raise Exception("This is an error")

    @handle_error
    def divide_numbers(x, y):
        return x / y

    assert example() is None
    assert divide_numbers(1, 0) is None


def test_hello():
    @hello("🌈")
    def world():
        return "world"

    assert world() == "hello world: 🌈"


def test_decorator():
    @decorator
    def function(input: str) -> str:
        return "output from " + input

    assert function("function") == "decorated output from function"


def test_stacked():
    @decorator
    @hello("😵‍💫")
    @decorator
    def function(input: str) -> str:
        return "output from " + input

    assert function("function") == "decorated hello decorated output from function: 😵‍💫"


def test_decorated_lambda():
    function = decorator(lambda string: string)
    assert function("lambda") == "decorated lambda"


def test_decorator_with_argument():
    @decorator_maker("decorated")
    def function(arg: str) -> str:
        return "output from " + arg

    assert function("function") == "decorated output from function"

from src.examples.snippet.src.decorator import handle_error, hello, decorator


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

    assert function("function") == "output from function"

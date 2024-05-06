from src.projects.examples.src.decorator import handle_error, hello


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

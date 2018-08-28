"""
Experiments on yield
"""

import math


def show_me():
    print("""
    Yield creates a generator, meaning:
    
        - You need to iterate through what the yield sent to get the next data
        - You do not need to wait for the return of the processing of a huge list
        - You can do unknown or infinite loops
        _ You can have special condition to make it stop defined
        - Pratice will yield its fruits
        
    Sources:
    
        - https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
        - https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
    
    
    """)


def basic_yield():
    yield 1
    yield 2
    yield 3


def normal_yield():
    for i in range(4, 7):
        yield i


def infinite_yield(n):
    number = n
    while True:
        if number < 11:
            yield number
        else:
            break  # The infinite loop
        number += 1


def use_yield_function(yield_function, *args):
    for value in yield_function(*args):
        print(value)


"""
generators the power to yield a value (as before), receive a value, 
or both yield a value and receive a (possibly different) value in a single statement.
"""


def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False


def get_primes(number):
    while True:
        if is_prime(number):
            number = yield number
        number += 1


def print_successive_primes(iterations, base=10):
    """
    we'll find the smallest prime number greater than successive powers of a number
    (i.e. for 10, we want the smallest prime greater than 10, then 100, then 1000, etc.)
    """
    prime_generator = get_primes(base)  # The function with the yield inside
    prime_generator.send(None)  # You can "send" values to a generator using the generator's send method.
    for power in range(iterations):
        print(prime_generator.send(base ** power))  # Try every value until it reaches base ** power and yield number
        # Try again with the next base ** power received in number.


class Bank():  # Let's create a bank, building ATMs
    crisis = False

    def __init__(self):
        print("\nA new bank is created")

    def create_atm(self):
        while not self.crisis:
            yield "$100"


if __name__ == "__main__":
    show_me()
    use_yield_function(basic_yield)
    use_yield_function(normal_yield)
    use_yield_function(infinite_yield, 7)
    print_successive_primes(10)

    hsbc = Bank()  # When everything's ok the ATM gives you as much as you want
    corner_street_atm = hsbc.create_atm()
    print(next(corner_street_atm))

    print(next(corner_street_atm))

    print([next(corner_street_atm) for cash in range(5)])

    hsbc.crisis = True  # Crisis is coming, no more money!
    try:
        print(next(corner_street_atm))
    except StopIteration as e:
        print("StopIteration stopped because of crisis")

    wall_street_atm = hsbc.create_atm()  # It's even true for new ATMs
    try:
        print(next(wall_street_atm))
    except StopIteration as e:
        print("StopIteration stopped because of crisis even for new ATMs")

    hsbc.crisis = False  # The trouble is, even post-crisis the ATM remains empty
    try:
        print(next(corner_street_atm))
    except StopIteration as e:
        print("StopIteration stopped because of crisis even after crisis")

    brand_new_atm = hsbc.create_atm()  # Build a new one to get back in business
    for cash in brand_new_atm:         # infinite loop
        print(cash)
        break

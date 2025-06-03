# Basic class definition


# EXAMPLE 1
class Dog:
    # self is always the first parameter
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def call_dog(self):
        print(f"Come here, {self.name}!")

    def speak(self):
        print("bark bark bark")


dog1 = Dog("Spot", 2)
dog1.call_dog()
dog1.speak()
print(f"dog1's name is {dog1.name}.")
# Spot

dog2 = Dog("Wally", 4)
dog2.call_dog()
dog2.age += 1
print(dog2.age)
# 5


# EXAMPLE 2
class Dog:
    _count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog._count += 1

    def call_dog(self):
        print(f"Come here, {self.name}!")

    def speak(self):
        print("bark bark bark")

    @classmethod
    def get_dog_count(cls):
        return cls._count


# Create a couple of dogs
dog1 = Dog("Spot", 2)
dog1.call_dog()
dog1.speak()
print(f"dog1's name is {dog1.name}.")

dog2 = Dog("Wally", 4)
dog2.call_dog()
dog2.age += 1
print(f"dog2's new age: {dog2.age}")

print(f"Total dogs created: {Dog.get_dog_count()}")
# Total dogs created: 2

# Class inheritance

# EXAMPLE 3


class BigDog(Dog):  # inherits from Dog
    def __init__(self, name, age):
        # Call the parent class's __init__ to set name/age
        super().__init__(name, age)

    def fetch(self):
        print("Got it.")

    def speak(self):
        print("Woof Woof Woof")  # overrides Dog.speak()

    def speak_verbose(self):
        # call Dog.speak(), then BigDog.speak()
        super().speak()
        self.speak()


dog3 = BigDog("Butch", 3)
dog3.call_dog()
dog3.speak()
dog3.speak_verbose()
BigDog.get_dog_count()

# print(BigDog.__dict__) # prints attributes and methods for the Dog class
# {
# '__module__': '__main__',
# '__init__': <function BigDog.__init__ at 0x123da2480>,
# 'fetch': <function BigDog.fetch at 0x123da2520>,
# 'speak': <function BigDog.speak at 0x123da25c0>,
# 'speak_verbose': <function BigDog.speak_verbose at 0x123da2660>,
# '__doc__': None
# }
# print(Dog.__dict__) # prints attributes and methods for the Dog class
# {
# '__module__': '__main__',
# '_count': 3, '__init__': <function Dog.__init__ at 0x136376200>,
# 'call_dog': <function Dog.call_dog at 0x1363762a0>,
# 'speak': <function Dog.speak at 0x136376340>,
# 'get_dog_count': <classmethod(<function Dog.get_dog_count at 0x1363763e0>)>,
# '__dict__': <attribute '__dict__' of 'Dog' objects>,
# '__weakref__': <attribute '__weakref__' of 'Dog' objects>,
# '__doc__': None
# }

print(dog1.__dict__)  # prints the attributes of the instance and their values.
# {'name': 'Spot', 'age': 2}


class Shout(str):
    def __new__(cls, content):
        return str.__new__(cls, content.upper())


x = Shout("hello there")
print(x)  # prints HELLO THERE

#  Introduction to Decorators


# EXAMPLE
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return 3.14 * self.radius**2

    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(3)
print(c.area)
# 28.26
print(c.diameter)
# 6

c.radius = 5
print(c.area)
# 78.5

# EXAMPLE 2
# @dataclass decorator, which lets you quickly and
# conveniently define simple classes for storing
# structured data, without needing an __init__ method.
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str


book1 = Book("Dune", "Frank Herbert")
book2 = Book("Dune", "Frank Herbert")
book3 = Book("Neuromancer", "William Gibson")

print(book1)
print(book2.title)
print(book1 == book2)  # True — same data, so considered equal
print(book1 == book3)  # False — different data


# EXAMPLE 3
def say_hello():
    print("Hello!")


def repeat_me(func, num_repeats):
    for _ in range(num_repeats):
        func()


repeat_me(say_hello, 5)  # Will print "Hello!" 5x


def my_decorator(func):
    def wrapper():
        print("Hello!")
        func()
        print("World!")

    return wrapper


@my_decorator
def print_name():
    print("John")


print_name()

# Hello!
# John
# World!

# EXAMPLE 3
# Decorator that will work with any function

import time


def timer(func):
    ## Output the time the inner function takes
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished in {run_time:.4f} secs")
        return value

    return wrapper_timer


@timer
def wait_half_second():
    time.sleep(0.5)
    return "Done"


wait_half_second()

# EXAMPLE 5


def repeat_with_prefix(prefix, num_repeats):  # decorator factory
    def decorator(func):  # The decorator: takes the function
        def wrapper(
            *args, **kwargs
        ):  # The wrapper: runs the function with extra behavior
            for _ in range(num_repeats):
                result = func(*args, **kwargs)  # Call the original function
                print(f"{prefix} {result}")

        return wrapper

    return decorator


@repeat_with_prefix(">>", 3)
def greet(name):
    return f"Hello, {name}!"


greet("Amanda")

# >> Hello, Amanda!
# >> Hello, Amanda!
# >> Hello, Amanda!


# THEORATICAL
# Decorators are often used in another way.
# They register a function that is to be called by system code.
# For example, in the lesson on Dash, you had the following lines:

# @app.callback(
#     Output("stock-price", "figure"),
#     [Input("stock-dropdown", "value")]
# )
# def update_graph(symbol):

# The app.callback method runs before update_graph() is ever called.
# It records the fact that update_graph(),
# as wrappered by the app.callback wrapper function,
# is to be called whenever the stock dropdown changes.
# You could do something like this, registering the functions
# to be wrapped, as follows:

callback_dict = {}


def wrap_output(before, after, greeting_type):
    def decorator_wrap_output(func):
        callback_dict[greeting_type] = func

        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return before + result + after

        callback_dict[greeting_type] = wrapper
        return wrapper

    return decorator_wrap_output


@wrap_output("begin:", ":end", "for_hello")
def hello():
    return "Hello, World!"


@wrap_output("begin:", ":end", "for_goodbye")
def goodbye():
    return "Goodbye, World!"


print(callback_dict["for_hello"]())  # Will print "begin:Hello, World!:end"

print(callback_dict["for_goodbye"]())  # Will print "begin:Goodbye, World!:end"

# Here, the decorated functions, in their wrappered form, get registered for callbacks in callback_dict.
# This is like what Dash is doing when you use the decorator @app.callback.

# List Comprehensions
integer_list = []
for x in range(20):
    integer_list.append(x)
# but, with Python, you can use a list comprehension as a shorthand:

integer_list = [x for x in range(20)]
# Or, to get just the odd ones:

odd_list = [x for x in range(20) if x % 2 != 0]
# Or, to get the squares of the odd ones:

odd_squares_list = [x**2 for x in range(20) if x % 2 != 0]
# or
odd_squares_list = [x**2 for x in odd_list]

# A generator expression is just like a list comprehension,
# except that you use parentheses instead of square brackets.
# A generator expression is an iterable, meaning you can use it in a for loop.
# Like so:

odd_squares_generator = (x**2 for x in range(20) if x % 2 != 0)

for y in odd_squares_generator:
    print(y)


#  Python Closures


def make_secret(secret):
    def did_you_guess(guess):
        if guess == secret:
            print("You got it!")
        else:
            print("Nope")

    return did_you_guess


game1 = make_secret("swordfish")
game2 = make_secret("magic")

game1("magic")  # Prints nope
game1("swordfish")  # Prints you got it
game2("magic")  # Prints you got it


def make_secret(secret):
    bad_guesses = 0

    def did_you_guess(guess):
        nonlocal bad_guesses
        if guess == secret:
            print("You got it!")
        else:
            bad_guesses += 1
            print(f"Nope, bad guesses: {bad_guesses}")

    return did_you_guess


game1 = make_secret("swordfish")
game1("magic")  # Prints nope, bad guesses 1
game1("magic")  # Prints nope, bad guesses 2

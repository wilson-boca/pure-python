from functools import wraps
import time


#  functions are aldo objects in python, first class functions
def say_name():
    print("Wilson Rodrigo")


def say_nationality():
    print("Brazilian")


def say(func):
    return func


# say(say_name)()
# say(say_nationality)()


# inner functions
def say():

    def say_name():
        print("Wilson Rodrigo")

    def say_nationality():
        print("Brazilian")

    say_name()
    say_nationality()


some_var = say
# some_var()


def say(func):

    def employer():
        print("Say something about you.")

    def say_name():
        print("My name is Wilson Rodrigo...")

    def say_nationality():
        print("I am from Brazil!")

    def wrapper():
        employer()
        say_name()
        say_nationality()
        func()

    return wrapper


@say
def start_interview():
    print("Real interview Started...")


# start_interview()


# wrappers with arguments
def say(func):

    def wrapper(*args, **kwargs):
        print('From wrapper!!!')
        print(f' Args: {args}')
        print(f' Kwargs: {kwargs}')
        func(*args, **kwargs)
    return wrapper


@say
def greet(*args, **kwargs):
    print('From greet!!!')
    print(*args)
    keys, values = [(row, kwargs[row]) for row in kwargs]
    print(keys)
    print(values)
    print({row: kwargs[row] for row in kwargs})


greet('Wilson', 'Rodrigo', 'Patricio', 'Ferreira', language="Python", position='Developer')
print('The greet function name is ->{}<-, weird...'.format(greet.__name__))


def logged(func):
    # try comment the line below to see what happens
    @wraps(func)
    def with_logging(*args, **kwargs):
        """replaced by with_logging function"""
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging


@logged
def my_original(x):
   """my_original does some math"""
   return x + x * x


res = my_original(5)
print(my_original.__name__)  # prints 'f'
print(my_original.__doc__)   # prints 'does some math'


# a very nice and useful decorator


def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        if run_time > 60:
            print("Finished {} in {} mins".format(repr(func.__name__), round(run_time / 60, 2)))
        else:
            print("Finished {} in {} secs".format(repr(func.__name__), round(run_time, 2)))
        return value

    return wrapper


@timer
def doubled_and_add(num):
    res = sum([i * 2 for i in range(num)])
    # delayer
    for i in range(num):
        time.sleep(5)
    print("Result : {}".format(res))


doubled_and_add(2)
doubled_and_add(13)

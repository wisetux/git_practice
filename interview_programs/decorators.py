import functools
import time


def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


def timer(func):
    """prints the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.time()
        value = func(*args, **kwargs)
        end_time = time.time()
        print("time taken for the execution of function {} is {}".format(func.__name__, end_time-start_time))
        return value
    return wrapper_timer
@timer
def waste_some_time(num_of_times):
    for _ in range(num_of_times):
        time.sleep(3)




import functools

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)           # 3
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # 4
        return value
    return wrapper_debug

@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}!"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"
make_greeting("Anil kumar pathapati")



def sample_decorator(original_function):
    def wrapper_function(*args, **kwargs):
        print(" i am inside wrapper")
        original_function()
    return wrapper_function

@sample_decorator
def display():
    print("hello")
display()

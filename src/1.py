def show_message():
    def wrapper(func):
        def inner(*args, **kwargs):
            print("Before run function")
            result = func(*args, **kwargs)
            print("After run function")
            return result
        return inner
    return wrapper

# Usage as decorator

@show_message()
def func1():
    print("In Function")

func1()
# Before run function
# In Function
# After run function

# Usage as function call
def func2():
    print("In Function")

show_message()(func2)()



def compare(a, b, *, key=None):
    ...

compare(1, 2, key=lambda x: x) # OK
compare(1, 2, lambda x: x) # Throws TypeError

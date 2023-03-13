def double(func):
    def inner_func():
        print("Let's try that again!")
        func()
        print("Let's try that again!")
    return inner_func

@double
def hello():
    print("Hello World")

hello()
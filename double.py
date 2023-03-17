def double(func):
    def inner_func():
        func()
        print("Let's try that again!")
        func()
    return inner_func

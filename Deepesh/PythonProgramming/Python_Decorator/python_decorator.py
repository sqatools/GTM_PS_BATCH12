# Decorator enhanace the functionality of existing code without changing the exiting code.

def greeting_decore(func):
    def inner(param):
        print("*"*50)
        func(param)
        print("*"*50)
    return inner


@greeting_decore
def greeting(msg):
    print(msg)


greeting("Hello good morning")
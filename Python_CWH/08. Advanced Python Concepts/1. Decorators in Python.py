#Decorators in Python
# Decorator is a function that takes a function,it creates a new function inside its body(wrapper).Then it returns that new function
# def decorator(func):
#     def wrapper():
#         print("I am about to execute a function....")
#         func()
#         print("I have executed this function....")
#     return wrapper
# @decorator
# def say_hello():
#     print("Hello")

# say_hello()
# # say_hello()
# # f = decorator(say_hello)
# # f() 

# Decorators with arguments
def repeat(n):
    def decorator(func):
        def wrapper(a):
            for in range(n):
                func(a)
        return wrapper
    return decorator
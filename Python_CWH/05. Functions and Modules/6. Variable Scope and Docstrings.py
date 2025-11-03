# 6. Variable Scope and Docstrings

# def sum(a, b):
#     c = a + b
#     # print(z)
#     z = 1
#     return c
# def greet():
#     z = 32
#     print("GHOST")

# z = 8
# print(sum(4,6))
# print(z)


# Global Keyword
# def sum(a,b):
#     c = a + b
#     global z
#     z = 0
#     return c

# z = 3
# print(sum(3,12))
# print(z)


# Docstrings
def sum(a,b):
    '''This will sum two numbers'''
    c = a + b
    return c 

print(sum.__doc__)
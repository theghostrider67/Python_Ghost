# Function Arguments & Return Values

# Positional Arguments
# def add(a,b):
#     x = a+b
#     return x

# c = add(3,5)
# print(c)

# Default Arguments
# def add(a,b, plus=0):
#     x = a + b + plus
#     return x
# c = add(3,5,2)
# print(c)

# Keyword Arguments
def add(a,b, plus=0):
    x = a + b + plus
    return x
c = add(3,5,2)
print(c)

c1 = add(b=5,a=3)
print(c1)


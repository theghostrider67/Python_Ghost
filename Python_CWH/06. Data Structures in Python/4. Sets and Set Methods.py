# Sets

# fruits = {"Apple", "Mango", "Lichi"}

# number = {3, 23, 2, 11}
# print(number, type(number))
# print(fruits, type(fruits))
# print(number[3]) # Like a basket that has no order


# Set Methods

# s = {3, 23, 2, 11, 41}
# print(s)
# s.add(22) 
# s.remove(11)
# s.add(322)
# # s.remove(323342) #Trows errors
# s.discard(323342)
# print(s)


# Set operations
a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

c = a.union(b)
print(c)

d = a.intersection(b)
print(d)

e = a.difference(b)
print(e)
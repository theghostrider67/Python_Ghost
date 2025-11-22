# Read
# f = open("Read.txt", "r")
# content = f.read()
# print(content)
# f.close()

# Write
# f = open("GHOST.txt", "w")
# string = '''
# Ghost is a very nice guy. He lives in Milan and he works with.
# His favourite is numpy
# He is a ghost
# '''
# f.write(string)
# f.close()

# Append
# f = open("GHOST.txt", "a")
# string = '''
# Ghost is a CSE student at AIUB
# '''
# f.write(string)
# f.close()

# Line By Line
# f = open("Ghost.txt","r" )
# for  line in f:
#     print(line)
# f.close()

# With
# f = open("Read.txt", "r")
# # content = f.read()
# print(f.read())
# f.close()
with open("Read.txt", "r") as f: #Context manager
    content = f.read()
    print(content)
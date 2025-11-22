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
f = open("GHOST.txt", "a")
string = '''
Ghost is a CSE student at AIUB
'''
f.write(string)
f.close()
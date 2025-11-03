#4. String Formatting and f-Strings

template = "Dear {}, you are best. Take this ${} bag."
a = "John"
a1 = 10000
b = "Jack"
b1 = 1000
c = "Marie"
c1= 300

# s1 = template.format(a, a1)
# s2 = template.format(b, b1)
# s3 = template.format(c, c1)
# print(s1)
# print(s2)
# print(s3)

print(f"{a} you are best. Take this ${a1} bag")
print(f"{b} you are best. Take this ${b1} bag")
print(f"{c} you are best. Take this ${c1} bag")

print("Alhamdulillah")
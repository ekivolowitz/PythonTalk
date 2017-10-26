a = 256
b = 256
print("a == {0}".format(a))
print("b == {0}".format(b))
# In python, numbers <= 256 are cached
print("a is b? {0}".format(a is b)) # True
print("a is not b? {0}".format(a is not b)) # False
a += 1
b += 1
print("a == {0}".format(a))
print("b == {0}".format(b))
print("a is b? {0}".format(a is b)) # True
print("a is not b? {0}".format(a is not b)) # False
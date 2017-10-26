f = open("test_file.txt", 'w')
f.write("test\n")
f.write("for\n")
f.write("writing\n")
f.write("to files\n")
f.close()

# Equivalent to the iterative solution below.
# f = open('test_file.txt', 'r')
# for line in f:
#     line = line.replace("\n", "")
#     print(line)
# f.close()

print("Iteratively")
with open('test_file.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''))
print()
print("with .read()")
with open('test_file.txt') as f:
    wholeFile = f.read()
    
    print(str(wholeFile))
    
print("with .readline()")
with open('test_file.txt') as f:
    firstLine = f.readline()
    print(str(firstLine))

print("with .readlines()")
with open('test_file.txt') as f:
    listOfLines = f.readlines()
    print(str(listOfLines))
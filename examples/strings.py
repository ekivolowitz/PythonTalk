# This is an example of string formatters
testString = "Evan really likes the numbers {0}, {1}, {2}".format(12,20,420)
print(testString)

# This is an example of reversing a string
print("The reverse of \n{0}\nis\n{1}".format(testString, testString[::-1]))

# Tests capitalize and isalpha
for letter in testString:
    if letter.isalpha():
        print(letter.capitalize())
# The power of split
tokenized = testString.split(" ")
for value in tokenized:
    value = value.replace(",", "")
    print(value)
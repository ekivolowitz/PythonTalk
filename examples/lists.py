

list1 = [1,2,3,4,5]
print(str(id(list1)) + " | " + str(list1))

list1[3] = 10
print(str(id(list1)) + " | " + str(list1) + "\n\n")


reversedList = list1[::-1]
# print(str(id(list1)) + " | " + str(list1))
print(str(id(reversedList)) + " | " + str(reversedList))

print("What are the third, fourth, and fifth elements of list1?")
print(list1[2:5]) # [0:2:-3]
print("What is every even indexed element of list1?")
print(list1[::2])

# Here is extending two lists together:
list1.extend(reversedList)
print(str(list1))

list1 = [1,2,3,4,5]
reversedList = list1[::-1]

# Here is appending two lists together
print("list1 is " + str(list1))
list1.append(reversedList)
print(list1)

print("What is the index element 3? {0}".format(list1.index(3)))

### List comprehension

list1 = list1[:-1]

print("Let's make a list of the square of each value of list1")
print(str([num ** 2 for num in list1]))

print("Let's print only the even numbers in the square of list1")
evenSquares = [x ** 2 for x in list1 if x ** 2 % 2 == 0]
 
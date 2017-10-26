
from dollar import nationality as n
print(n)

for i,word in enumerate(['list', 'of', 'names']):
    print(str(i) + " " + word)

x = 0
while x < 10:
    print(x)
    x += 1

if x > 5:
    print('x is greater than 5')
elif x >= 10:
    print('x is greather than or equal to 10')
else:
    print('x is > 10')

for x in range(10):
    print(x)

for x in range(20):
    if x % 2 == 0:
        continue
    elif x == 17:
        break
    else:
        print(x)

def isEven(num):
    return num % 2 == 0

'''
TODO: P vs NP
'''
def PvsNP():
    pass


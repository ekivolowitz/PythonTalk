from pprint import pprint

print("Let's make a dictionary d")
d = {}

aDictionary = {}

aDictionary['Eric'] = "Pepperoni"

print(aDictionary['Eric'])

d['People'] = {}
d['People']['Evan'] = {}
d['People']['Eric'] = {}
d['People']['Evan']['Name'] = "Evan"
d['People']['Evan']['Age'] = 21
d['People']['Evan']['FavMovies'] = ['Monty Python and the Holy Grail', 'Step Brothers']
pprint(d)


# Super cool function in python that isn't widely used, but is the perfect tool for the job when used.
names = ['Evan', 'Spencer', 'Morgan']
ages = [10, 20, 30]

namesAndAges = dict(zip(names, ages))

pprint(namesAndAges)

namesAndAges['Evan'] = 21

pprint(namesAndAges)

print(str(list(namesAndAges.keys())))
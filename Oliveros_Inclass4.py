#Inclass4 Part 2

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

print "I will now count my chickens:"
#prints the text in quotes
print "Hens", 25 + 30 / 6
#prints the results of the arithmetic operation: 30
print "Roosters", 100 - 25 * 3 % 4
#prints roosters followed by the results of the arithmetic operation
print "Now I will count the eggs:"
#prints the text in quotations
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
#prints the result of the arithmetic operation: 7
print "Is it true that 3 + 2 < 5 - 7?"
#prints the text in quotations
print 3 + 2 < 5 - 7
#prints false because 3+2 = 5 > (5-7) 
print "What is 3 + 2?", 3 + 2
#prints the text in quotes followed by 5
print "What is 5 - 7?", 5 - 7
#prints the text in quotes followed by -2
print "Oh, that's why it's False."
#prints the text in quotations
print "How about some more."
#prints the text in quotations
print "Is it greater?", 5 > -2
#prints text in quotes followed by true because 5 is greater than -2
print "Is it greater or equal?", 5 >= -2
#prints text in quotes followed by true because 5 is greater than -2
print "Is it less or equal?", 5 <= -2
#prints text in quotes followed by false because 5 is not less than or equal to -2
#PART II

days = "Mon Tue Wed Thu Fri Sat Sun"
#sets days equal to the text in quotes
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
#sets months equal to the text in quotes each month in a new line

print "Here are the days: ", days
#prints the text in quotes followed by the text stored in days
print "Here are the months: ", months
#prints the text in quotes followed by the text stored in months

#PART III

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
#sets the variables equal to the corresponding values
# 
for number in the_count:
    print "This is count %d" % number
#for every element in "the_count" it prints the text in quotes 
# followed by the number
#
for fruit in fruits:
    print "A fruit of type: %s" % fruit
#iterates through fruits and prints out the text in quotes
#followed by the element in fruits
# 
# Use %r format when you don't know
#if the elements are strings or integers
for i in change:
    print "I got %r" % i
#Iterates through change and prints out the text in quotes followed
#by the element in change

# we can also build lists, first start with an empty one
elements = []
#initiates an empty list

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)
#starting at 0, runs the for loop 6 times and prints the text
#in quotes and the %d gets replaced by %i
#the i's also get appended to elements
for i in elements:
    print "Element was: %d" % i
#for every element in elements it prints the text in quotes and
# the %d gets replaced by the %i

######################

#Inclass4 Part 3

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

#Use the code from Lecture14.py to create and change the 
#'stuff' list; Then comment on each line of the code below
#what it does, and what the result is

ten_things = "Apples Oranges Crows Telephone Light Sugar"

#print "Wait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
#while the length of stuff isn't 10, pop the first element from more_stuff
# and append it to stuff.
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "The 'stuff' list: ", stuff


print stuff[1]
#prints the second element in stuff
print stuff[-1]
#prints the last element in the list
print stuff.pop()
#pops the last element in the list
print ' '.join(stuff) 
#prints the elements in the list separated by a space
print '#'.join(stuff[3:5]) 
#prints the third element followed by # and the fourth element
#PART II

#Create comments where marked with # to explain the code below

#sets the states and their two letter acronym equivalent to each other
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# sets the cities and their state acronym equivalent to each other
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# sets the values NY and OR in cities equal to their equivalent city
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# prints 10 of "-" 
# prints text in quotes followed by the equivalent city in cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# prints text in quotes followed by the equivalent state acronym
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# prints the text in quotes followed by the equivalent city of the state
# specified
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# for every element in state, it prints the text in quotes
# the %s are replaced by the state and then the abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# for every element in cities it prints the text in quotes
# the %s is replaced by the abbreviation and then the city
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# for every element in states it prints the text in quotes
# the %s is replaced by the state, then the abbreviation, and lastly
# the city of the abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])



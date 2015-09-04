the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count:
    print "This is count %d" % number


for fruit in fruits:
	print "This is the type %s" % fruit


for i in change:
    print "I got %r" % i


elements = []

for i in range(0,6):
	print "Insert %d into an elements array" % i 
	elements.append(i)

print elements

for element in elements:
	print "Element was %d" % element
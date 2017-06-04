my_name = "John Smith"
my_age = 42 # not a lie
my_height = 76
my_weight = 185
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Grey"

print "Let's talk about %s." % my_name
print "He's %d inces tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)

# This line is tricky, try to get it exactly right.
print "If I add %d, %d, and %d I get %d." %(
        my_age, my_height, my_weight, my_age + my_height + my_weight)

# Study Drill 1
print "\n"
name = "John Smith"
age = 42 # not a lie
height = 76
weight = 185
eyes = "Blue"
teeth = "White"
hair = "Grey"

print "Let's talk about %s." % name
print "He's %d inces tall." % height
print "He's %d pounds heavy." % weight
print "Actually, that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)

# This line is tricky, try to get it exactly right.
print "If I add %d, %d, and %d I get %d." %(
        age, height, weight, age + height + weight)

print
inches = 5
centimeter_conversion = 2.54
print "%d inches in centimeters = %f" % (inches, inches * centimeter_conversion)

print
pounds = 3
kilogram_conversion = 0.454
print "%d pounds in kilograms = %f" % (pounds, pounds * kilogram_conversion)

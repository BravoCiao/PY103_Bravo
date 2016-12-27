my_name = 'Bravo Ciao'
my_age = 24
my_height = 152 # cms
my_weight = 54 # kms
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'
my_height_inches = 0.39 * my_height # inches
my_weight_lbs = 2.20 * my_weight # lbs

print "Let's talk about %s." % my_name
print "I'm %s inches tall." % my_height_inches
print "I'm %s lbs heavy." % my_weight_lbs
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
# why the calculation can't be achieved inside the string?

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
# if you replace all the %d with %s, the result is the same
# %s for string, #d for decimal
# python only allows 80 characters per line.

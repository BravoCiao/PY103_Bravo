my_name = 'Bravo Ciao'
my_age = 24
my_height = 152 # cms
my_weight = 54 # kms
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "I'm %d cms tall." % my_height
print "I'm %d kms heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)
# if you replace all the %d with %s, the result is the same
# %s for string, #d for decimal
# python only allows 80 characters per line.

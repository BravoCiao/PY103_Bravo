x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print x
print y
# y is a string in string, but i don't think x is a string in string
# studydrill 2

print "I said: %r." % x
print "I also said: '%s'." % y
# the above two prints are formatstring in formatstring studydrill 2

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# we don't define %r here in line 15

print joke_evaluation % hilarious
# now we define %r as hilarious in the variable joke_evaluation
# i don't think it's a string in string studydrill 2

w = "This is the left side of..."
e = "a string with a right side."

print w + e
# print two sentences without a space in between
print w, e
# print two sentences with a space in between

# why two strings can be combined by +?
# i don't think it's a string in string neither , so in total, i just find
# 3 string in string, why? studydrill 2

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
# def is a command for define
# print_two is the function's name
# *args is like the argv parameter but it's for function, it has to go inside
# the parentheses to work
# a colon: is for indenting, so from the next line, it will intend for
# four spaces and below the colon, that's for the function print_two
# four spaces mean something in python, but may not be necessary in other
# programmes


# ok, that *args is actually pointless, we can juxt do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."
# a function with no arguement still does something, it just doesn't ask
# added arguement to run the function

print_two("Bravo","Ciao")
print_two_again("Bravo","Ciao")
print_one("First!")
print_none()
# why there should be ""?
# why not give arg1 and arg2 their value and let them fill in the function?
# studydrill8 does the last four lines mean dedenting?

# common student questions
# What's allowed for a function name?
# The same as variable names. Anything that doesn't start with a number,
# and is letters, numbers, and underscores will work.

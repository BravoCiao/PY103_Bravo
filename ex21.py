def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b
# return makes the function return the result of calculation, any variable Can
# use this result as the value
# i try to print "Let's..." and the next few lines first, then give the
# definition, but it doesn't work, even if it's in the same file
# python read the programme line by line


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)
# if i delete the return line in add function, why can't the programme print
# Age: ADDING 30 +  5? Why it must be a number?

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# why it can print it line by line
# strat from the most inside parentheses is easier and go an outer one the next

print "That becomes: ", what, "Can you do it by hand?"
# have question about the second student question of raw_input(),
# int(raw_input()) and float(raw_input())

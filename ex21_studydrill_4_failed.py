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

print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here is a puzzle."

what = divide(age, multiply(height, subtract(weight, (add(multiply(divide,
(add(height, age(divide(weight, iq))))))))))
# i don't know how to deal with this lone what variable line,
# i've tried to use """, not adding a comma, adding a comma at the end
# none of them work, the error is 'int' object is not callable
print "That becomes: ", what, "Can you do it by hand?"

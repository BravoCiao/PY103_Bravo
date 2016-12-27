print "How old are you?",
age = raw_input("24")
# i've tried to delete the comma and run the programme,
# then the age shows,on the second line, the comma
# is a prompt for data to show on the same line.
# based on official handbook, raw_input() is written to standard output
# without a trailing newline. The function then reads a line from input,
# converts it to a string (stripping a trailing newline), and returns that.

print "How tall are you?",
height = raw_input()

print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)
# in %r, r is for representation, but will use the raw_input
# the contents between perentheses show the variable
# is in that order
# the first line end with an open perenthesis
# because of 80 characters limitation
# i try to put the answer in the perentheses of raw_input() without "",
# the answer shows in the first three prints, python didn't tell me
# to type in the answer, but the answer didn't show in the last two
# Then, i put the answer with "", and it works, python tells me to type in the
# answer and the answer shows in the last two prints
# conclusion is, if you didn't put anything inside the perentheses of
# raw_input(), the answer is typed in by yourself 

print
# to add a new line
print ("So, you're %r years old, %r cms tall, \n"
       "and %r kgs heavy.") % (age, height, weight)
# this is the video i see on Youtube about lpthw
# in that video, the uploader shows another way to
# write the code if we want to add more text into
# and that will excess the 80 character limitation
# put the sentence in the perentheses,
# this is called the adjacent string, the adjacent string
# will merge into one single string
# \n is to start a new line
# i checked the python handbook about the definition of raw_input
# but couldn't understand entirely

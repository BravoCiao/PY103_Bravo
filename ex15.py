from sys import argv
# from system import the argument variable

script, filename = argv
# the argument variables are script and filename

txt = open(filename)
# text is a variable, open is a command and inside () is the argv
# open(filename) is a set of command that opens the file object
# the command open opens a text file
# we use this file object as the variable txt's value

print "Here's your file %r:" % filename
print txt.read()
# here, we call a function on txt called read
# we put a dot behind txt to give file a command, the command is read
# i don't know why when it runs in Python, there is '' between filename
# i try to only type txt.read, without (), it doesn't work properly
# it says <built-in method read of file object at 0x01DFD1D8>
# i checked Youtube video,every function needs a place
# for argument to put additional information
# even there is nothing in the parentheses, you still need to keep it
# cause function has to have arguements

print "Type the filename again:"
file_again = raw_input("> ")
# raw_input() told you to type in the file name again

txt_again = open(file_again)
# file_again is the variable that we type in the filename, command open
# told you to open the file object we opened before,
# then, the file object we opened twice is the txt_again's value

print txt_again.read()
# Finally, we read the profile object in the txt_again

# i don't know what does it mean by only using raw_input in studydrill5
# i don't understand what does it mean in studydrill6

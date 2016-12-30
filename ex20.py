from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()
# where is f? there is no definition for f
# i've tried to replace f with anything, as long as it's not in conflict with
# any argv, variable definition in this grogramme
# i suspend it's a showing to substitute what we try to achieve in the code

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)
# i'm not sure what does function rewind make and why i need it
# so i deleted the function
# if i do this, the following programme can not show the lines
print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line= current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
# there are three current_line , how do you distinguish
# i changed the variable name to be current_line,_second
# and current_line_third,that's clearer to me, and it works the same
# current_line is the value respond to the value of line_count,
# but how does that respond to f.readline()?
# i tried to change the number of current_line to be 1,5,7
# the programme still read the text line by line
# so i suspend .readline() is a function to tell python read the text line
# by line, i didn't find the suitable definition from the official handbook
# that's the author's explaination,Inside readline() is code that scans each
# byte of the file until it finds a \n character, then stops reading the file
# to return what it found so far. The file f is responsible for maintaining
# the current position in the file after each readline() call,
# so that it will keep reading each line.
# the function readline() will add a \n at the end of each line

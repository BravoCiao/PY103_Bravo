from sys import argv

script, filename = argv
# i've tried to write word & powerpoint files, and it works

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."
# why this can erase a file that doesn't exist?

raw_input("?")
# raw_input() is here to let you type in the response

print "Opening the file..."
target = open(filename, 'w')
# i don't understand why there is a 'w' in the perentheses
# i've tried to run the programme without 'w', but in that case
# i can't erase a file that didn't exist， however, with 'w', i can

print "Truncating the file, Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# i don't understand \n should have ""

print "And finally, we close it."
target.close()

# based on my trying of running the programme with and without 'w'
# for the answer of studydrill5, i think with 'w', python creates a
# complete new file directly, it's ready to be written on
# to be honest, i couldn't understand python's handbook...

# i checked the Youtube video, if we type 'w' for writing, then python creates
# a new file, and the previous one will be deleted
# if we type 'a' for append, then python will open the old one
# to add more text
# r+ allows you to read AND write
# w+ allows you to write AND read
# but what's the difference between r+ and w+

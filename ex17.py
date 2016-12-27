from sys import argv
from os.path import exists
# notes from Youtube video, os.path is used because different operating
# systems (e.g.. Mac, Windows, Linux) specify files paths in different
# ways: "exists" is a function that returns "TRUE" if the file path is
# valid (i.e.. the file exists AND the user has permissions)
# returns "FALSE" if not

script, from_file, to_file = argv
# Need to give name of files that you are copying from and copying to in the
# command line when you run this python script

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()
# one line indata = open(from_file).read()
# i questioned why there should be a in_file, but i didn't work out the answer
# i got the answer from Youtube

print "The input file is %d bytes long" % len(indata)
# len() is a function that tells you the length of one string
# why there is no "" around indata?
# i've tried the one with a "", the programme still run, but the length
# of indata is much shorter

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)
# why can't we just use the out_file as the argv
# out_file = open(from_file)
# out_file.write(indata)

print "Alright, all down."

out_file.close()
in_file.close()

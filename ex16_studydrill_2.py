from sys import argv

script, filename = argv

txt = open(filename)

print "See, this is the new text i just write!"
print
print txt.read()
print "Nice,humm~?"

txt.close()
# at first, i didn't put script on the argv list, the programme didn't run
# and it shows TypeError: coercing to Unicode: need string or buffer, list found
# why?

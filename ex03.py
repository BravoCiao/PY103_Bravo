print "I will now count my chickens:"

print "Hens", 25 + 30 / 6
print "Roosters", 100 - 25 * 3 % 4
# % here is a modulus, it's the number remained when doing a divide calculation
# for example, 25 * 3 % 4 = 18 r 3

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
# Counting order is PEMDAS
# i've tried to use 2 & 3 to replace 1 in the 1 / 4, the result is still 0
# python will not round the numbers without floating point

print "Is it true that 3 + 2 < 5 - 7?"
# does that mean, when a line includes < >, it will not do the calculation?

print 3 + 2 < 5 - 7
# why it can say it's true or false? because the question has been posted?
# the question is just a string! can the computer read the string?

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2
# why they can show it's true or false, why not just print them out directly?

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % cheese_count
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
# why a \n here?
# then i checked the Youtube video, cause there is a \n in the function
# each print will show a blanket new line


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
# why we don't need to give variable amount_of_cheese and amount_of_crackers
# a value again? cause in the previous exercises, we give it first the print
# does that mean no matter wherever you give the variable, it will work
# the same
# studydrill 3 is hard to finish, a pit to be filled... 

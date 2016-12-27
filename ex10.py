tabby_cat = "\tI'm tabbed in."
# \t means insert a tab,
# it leaves certain amount of space from the start of line
# backslash in python means do not read this as normally you would
persian_cat = "I'm split\non a line."
# you don't have a space between the backslash, t and n means
# you don't want a space at the end of the first line
# or a space in the start of the second line
backslash_cat = "I'm \\ a \\ cat."
# \\means print one backslash, the first backslash means do not read it
# literally, and the socond is a character
# actually, i tried to put just one \ between the a, and it works the same
# as i typed \\
# backslash means zhuanyi
# "I am 6'2\" tall."  # escape double-quote inside string
# \ zhuanyile "
# 'I am 6\'2" tall.'  # escape single-quote inside string
# \ zhuanyile '

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Finishes
\t* Catnip\n\t* Grass
'''
# i tried to put space between \n and \t, i expected it to show more space
# before * Grass, but it didn't, i don't know why
# ''' works the same as """

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# didn't finish the study drill 3 & 4

formatter = "%r %r %r %r"
# %r can read any kind of data, it can read charater, string, floating point,
# and other variables, it works best for debugging
print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
# True and False are built-in key words that don't need quotes
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
# double quote inside double quote will turn out to be single quote

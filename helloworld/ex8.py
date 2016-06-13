# Formatting

formatter = "%r %r %r %r"


print formatter % (1,2,3,4)
print formatter % ('Shad', 'loves', 'Kim', '<3')
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

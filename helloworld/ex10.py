#escape double quote and single quote instances

fat_cat = "\tI'm a fat cat." # the '\t' is for tab
skinny_cat = "I'm a split \n on a line" #
backslash_cat = "I'm \\ a \\ cat."

the_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""


print fat_cat
print skinny_cat
print backslash_cat

print "\n", the_cat

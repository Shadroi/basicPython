#Exercise 6: Strings and Text

name = "Kim"
x = "There are %d things I love about %s" % (100, name)

name2 = "Shad"
y = "%s said that she's the best thing that ever happened to him." % name2


print "I said that %s" % x
print "He said that %r" % y

#understanding the '%s' it means that only for Strings
#while the '%d' is for number / integer
#while '%r' is to force it with punctuation marks


funny = False #boolean
a_joke = "isn't it funny?! %r" #forcing the boolean to show up without putting the value here

print a_joke % funny # as you can see the value of funny is added on the print instead on the string variable

left = "Left side of the sentence, "
right = "Right side of the sentence."

print left + right

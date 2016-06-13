#Woohoo! Input
import datetime #imported datetime class

year = datetime.date.today().year

print "What is your name?"
name = raw_input()

print "What year you wear born?"
raw_year = int(raw_input())
age = year - raw_year #computed age based on year born

print "How tall are you?"
height = raw_input()

print "How much do you weigh"
weight = raw_input()

print "Your name is %r, you're %r years old, %r tall and %r heavy." % (name,age,height,weight)

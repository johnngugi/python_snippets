# import argv module
from sys import argv

# assign the argument to a variable
script, filename = argv

# print out filename
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# add a prompt
raw_input("?")

# open the file
print "Open the file..."
target = open(filename, "w")

# truncate the file
print "Truncating file... Goodbye!"
target.truncate()

# write to the file
print "Now I'm going to write to these files"

line1 = raw_input("line 1: ")

print "I'm going to write to these files"

target.write(line1)
target.write("\n")

#close the file
target.close()



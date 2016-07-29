name = open("john.txt", "a")
newname = str(raw_input("What is your name?"))
name.read()
if name.find(newname):
    print "Error"
else:
    name.write(newname + "\n")
    name.close()
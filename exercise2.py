name = open("john.txt", "a")
newname = raw_input("What is your name?")
if type(newname) == str:
    name.write(newname + "\n")
    name.close()
from tribonaccif import tribonacci


def printer():
    print("enter a value")
    userinput = int(raw_input("How many sequences?"))
    # type(userinput)
    print tribonacci(userinput)

printer()
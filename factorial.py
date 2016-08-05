def factorial(n):
    # print str(n)
    if n == 1:
        return 1
    else:
        result = n * factorial(n-1)
        return result
        
def printer():
    s = int(raw_input("Which number?"))
    print factorial(s)
    
printer()
        

            


def fibonacci(n):
    
    a,b = 0,1
    result = []
    
    for i in range(n):
        result.append(b)
        a, b = b, a + b
        
    return result
    #=print result 
   
    
    
print fibonacci(20)

def fibonacci(number):

	a,b=1,1
	c = [1]

	while(a < number):

  		a,b=b,a+b
  		c.append(a)

  	return c

print fibonacci(20)

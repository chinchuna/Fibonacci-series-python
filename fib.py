number=int(raw_input("Enter the count: "))
a=0
b=1
c=0
print a
for i in range(number-1):
	c=a+b
	print c
	b=a
	a=c
	
	

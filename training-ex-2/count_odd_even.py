num = input("Enter the series of numbers:")
c = 0
d = 0
for i in range(1,num+1):
	if i%2 == 0:
		c += i
	else:
		d += i
print "The even count is:%s\nThe odd count is:"%c,d

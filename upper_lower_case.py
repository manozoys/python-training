a = raw_input("Enter the string:")
a = a.replace(" ","")
c = 0
d = 0
for i in a:
	if i.islower():
		c += 1
	else:
		d += 1
print "Number of Lower cases is:%s \nNumber of Upper cases is:"%c,d

a = raw_input("Enter the string:")
b = ''.join(reversed(a))
if a == b:
	print "Palindrome"
else:
	print "Not palindrome"

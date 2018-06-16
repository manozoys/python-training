#!/usr/bin/python
string = raw_input("Enter the string:")
sub_string = raw_input("Enter the sub_string:")
if sub_string in string:
	print "sub_string found"
else:
	print "sub_string not found"

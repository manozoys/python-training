#!/usr/bin/python
number = raw_input("Enter the list:")
number = number.split()
print "sorted list:", sorted(number)
print "Reverse sorting:", sorted(number, reverse = True)

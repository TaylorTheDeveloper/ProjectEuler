#!/usr/bin/env python

#Project Euler
# Problem 4: Largest Palindrome Product
 
valstr = "9009"
compstr = valstr[::-1]
val = 0;
largest = val;

if valstr == compstr:
	print "hey"

for i in range(100,999):
	for j in range(100,999):
		val = i*j
		valstr = str(val)
		compstr = valstr[::-1]
		if valstr == compstr:
			print val, i, j
			
			if val > largest:
				largest = val

print largest
		





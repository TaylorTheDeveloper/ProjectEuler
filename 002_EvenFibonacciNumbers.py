#!/usr/bin/env python

#Project Euler
# Problem 2: Even Fibonacci Numbers

a = 1
b = 2
c = a + b 
sum = b # First Even Num

while c < 4000000:
	c = a + b
	a = b
	b = c
	if c%1 == 0:
		if c%2==0:
			print c
			sum+=c

print sum


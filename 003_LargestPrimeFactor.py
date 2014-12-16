#!/usr/bin/env python

#Project Euler
# Problem 3: Largest Prime Factor

number = 600851475143
numx = 97
primelist = []

def isprime(num):
	for i in range(2,num):
		if num%i == 0:
			return False
	return True

for i in range (2,8000):
	if isprime(i):
		#primelist.append(i)
		if number%i==0:
			number/=i
			print number,i

print primelist









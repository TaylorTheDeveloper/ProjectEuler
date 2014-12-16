#!/usr/bin/env python

#Project Euler
# Problem 5: Smallest Multiple

num = 2520
count = 1
max = 0

while num < 7500:
	count = 1
	for i in range(1,20):
		if num%i == 0:
			print num,i
			count+=1
		if count > max:
			max = count
		if count == 20:
			print num
			break
	num+=1



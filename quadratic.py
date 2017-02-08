#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#一元二次方程

import math

def quadratic(a, b, c):

	if not isinstance(a, (int, float)):
		raise TypeError('a is bad operand type')

	if not isinstance(b, (int, float)):
		raise TypeError('b is bad operand type')

	if not isinstance(c, (int, float)):
		raise TypeError('c is bad operand type')

	if  a == 0:
		print('a can\'t equal zero')
		return 

	delta = b * b - 4 * a * c

	#if delta < 0 :
	#	print('no result!')

	x1 = (-b + math.sqrt(delta)) / (2 * a)

	x2 = (-b - math.sqrt(delta)) / (2 * a)
	
	return x1, x2


a = 3
b = 2
c = 1
print(quadratic(a, b, c))











# -*- coding: utf-8 -*-
import math 

x = float(input("\n test sk: "))

def sin_calculations_rad_deg(x):
	sk_radians = math.sin(x)
	sk_degrees = math.degrees(sk_radians)

	print "\n sin(%.2f) = radians(%.2f), degrees(%.2f) \n" %(x,sk_radians,sk_degrees)
	return; 

def sin_sum_int(x):
	s=0
	for i in range(0, int(x), 1):
		sk=(-1)**i*x**(2*i+1)/math.factorial(2*i+1)
		s+=sk
		print " a%i= %6.2f, \t s%i= %6.2f"%(i, sk, i, s)
	return;


sin_calculations_rad_deg(x)
sin_sum_int(x)

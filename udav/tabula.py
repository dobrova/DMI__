# -*- coding: utf-8 -*-
x = int(input("ievadiet skaitli: "))

for x in range(x, x+11, 1):
	print "%d \t"%(x),
	for i in range(1, 6, 1):
		sk_mod = x%i
		print "%d \t"%(sk_mod),
	print "\n"


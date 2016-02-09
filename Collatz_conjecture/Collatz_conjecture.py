#Collatz_conjecture https://en.wikipedia.org/wiki/Collatz_conjecture

def collatz(num_coll):
	z = num_coll
	num_cycles = 0
	while z > 1:
		if (z % 2) == 0:
			z = z / 2
			num_cycles += 1
		elif (z % 2) == 1:
			z = (z * 3) + 1
			num_cycles += 1
		print z
	print"Number Of Cycles -",num_cycles
	return ""
print collatz(32)
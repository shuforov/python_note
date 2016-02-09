#Collatz_conjecture https://en.wikipedia.org/wiki/Collatz_conjecture

def collatz(num_coll):
	z = num_coll
	while z > 1:
		if (z % 2) == 0:
			z = z / 2
		elif (z % 2) == 1:
			z = (z * 3) + 1
		print z

print collatz(142523423423423424663534752342352352352352)
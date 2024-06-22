# Problem
# Given: A file containing at most 1000 lines.
# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

f = open('./rosalind_ini5 (1).txt', 'r')

for index, line in enumerate(f):
	if index % 2 == 1:
		print(line, end='') 

f.close()

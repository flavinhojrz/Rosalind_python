# Problem
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.

# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

# Given: A DNA strings of length at most 1000 nt.

# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s

f = open('./rosalind_dna.txt', 'r')

a = 0
c = 0
g = 0
t = 0

for line in f:
  for dna in line.strip():
    if dna == "A":
      a += 1
    elif dna == "C":
      c += 1
    elif dna == "G":
      g += 1
    else:
      t +=1
    
print(a, c, g, t)
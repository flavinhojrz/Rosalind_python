# Problem
# An RNA string is a string formed from the alphabet containing 'A', 'C', 'G', and 'U'.

# Given a DNA string t
#  corresponding to a coding strand, its transcribed RNA string u
#  is formed by replacing all occurrences of 'T' in t
#  with 'U' in u

# Given: A DNA string t having length at most 1000 nt.
# Return: The transcribed RNA string of t

def transcribe_dna_to_rna(dna_string):
    rna_string = dna_string.replace('T', 'U')
    return rna_string
  
f = open('./rosalind_rna.txt', 'r')
s = f.read()
f.close()

print(transcribe_dna_to_rna(s))


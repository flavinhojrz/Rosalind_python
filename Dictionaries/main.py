# Problem
# Given: A strings of length at most 10000 letters.
# Return: The number of occurrences of each word in s, where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

def count_word_occurrences(s):
	words = s.split()
	word_count = {}
	
	for word in words:
		if word in word_count:
			word_count[word] += 1
		else:
			word_count[word] = 1
					
	return word_count

f = open('./rosalind_ini6 (1).txt', 'r')

s = f.read()

f.close()

word_count = count_word_occurrences(s)

for word, count in word_count.items():
  print(f"{word} {count}")

def break_words(stuff):
	word = stuff.split(' ')
	return word

word1 = break_words("james is just beautiful")
print word1

def sorted_words(words):
	return sorted(words)

print sorted_words(word1)

def print_first_word(words):
	word = words.pop(0)
	print word

print print_first_word(word1)
print word1
#the first index in the array has been removed



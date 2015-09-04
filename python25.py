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


def print_last_word(words):
	word = words.pop(-1)
	print word

print print_last_word(word1)
print word1


sentence1 = "james is just too handsome too beautiful"
def sort_sentence(sentence):
	word = break_words(sentence)
	return sorted_words(word)

print sort_sentence(sentence1)

def print_first_and_last(sentence):
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

print print_first_and_last(sentence1)




def capitalizeVowels(word):
    for letter in word:
        if letter in 'aeiou':
            capletter = letter.upper()
            word = word.replace(letter, capletter)
    return word
    
#Method 2
def capitalizeVowels(word):
	wordlist = list(word)
	vowel = 'aeiou'
	for l in wordlist:
		if l in vowel:
			newL = l.upper()
                        wordlist[wordlist.index(l)] = newL
	return ''.join(wordlist)
from random import randint,random
import requests

def get_word():
	word_site = 'http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain'
	response = requests.get(word_site)
	words = response.content.splitlines()
	word = (words[randint(0,len(words)-1)])
	wordstr= str(word)
	game_word = (wordstr.lower())
	return game_word

game_word = get_word()
word_break = list(game_word)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
display = []
incorrect = []
correct = []

for letter in word_break:
	display.append("_")

print(display)
print(incorrect)
#print(word_break)

while len(incorrect) < 7 and display != word_break:

	guess = raw_input("Can you guess the word? If you enter seven letters that are not in the word, the game is over!  Enter a letter! ").lower()
		
	try:
		guess
	except str:
		pass

	if guess in alphabet and guess in word_break:

		correct.append(guess)

		display = [letter if guess == letter else "_" for letter in word_break]
		display = [letter if letter in correct else "_" for letter in word_break]

	if guess in alphabet and guess not in word_break:

			incorrect.append(guess)

	if guess not in alphabet:

		print ("Invalid entry! You need to enter a letter in the english alphabet.")

	print(display)
	print('incorrect', incorrect)
	#print(word_break)
	print('correct', correct)
	
	if display == word_break:
		print('Congratulations!! You smart cookie, you.')

	if len(incorrect) == 7:

		print("Nope! Try again?!")

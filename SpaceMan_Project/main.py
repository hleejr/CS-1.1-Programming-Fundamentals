def game():
	import random
	
	blank = []
	correct = []
	incorrect = []

	def get_word():
		f = open('words.txt', 'r')
		words_list = f.readlines()
		f.close()
		
		words_list = words_list[0].split(' ')
		secret_word = random.choice(words_list)
		return secret_word

	def check_guess(letter):
		alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

		if letter not in alphabet:

			print ("Invalid entry! You need to enter ONE letter from the english alphabet.")

	def make_display(word):
		for letter in word:
			blank.append("_")

		return blank

	def check_word(letter, word):
		global blank

		if letter in word:
			correct.append(guess)

			blank = [letter if guess == letter else "_" for letter in word_break]
			blank = [letter if letter in correct else "_" for letter in word_break]
			return blank

		elif letter not in word and letter not in incorrect:
			incorrect.append(guess)

			blank = [letter if guess == letter else "_" for letter in word_break]
			blank = [letter if letter in correct else "_" for letter in word_break]
			return blank
		
		elif letter.isalpha() == False or len(letter) != 1 :
			print("Invalid entry")

			blank = [letter if guess == letter else "_" for letter in word_break]
			blank = [letter if letter in correct else "_" for letter in word_break]

			return blank

		else:
			print("Invalid entry!")

			blank = [letter if guess == letter else "_" for letter in word_break]
			blank = [letter if letter in correct else "_" for letter in word_break]

			return blank
	
	word_break = list(get_word())
	make_display(word_break)
	display = " ".join(blank)
	
	print (word_break)
	print(display)
	print("incorrect", incorrect)
	print("correct", correct)
	
	blank = []
	correct = []
	incorrect = []

	while len(incorrect) < 7 and blank != word_break:
		guess = input("Can you guess the word? If you enter seven letters that are not in the word, the game is over!  Enter a letter! ").lower()
		
		check_guess(guess)
		blank = check_word(guess, word_break)
		display = " ".join(blank)

		print(display)
		print("incorrect", incorrect)
		print("correct", correct)
					
		if list(blank) == word_break:
			print('Congratulations!! You smart cookie, you.')
					
		if len(incorrect) == 7:

			print("The word was {}! Try again?!".format(" ".join(word_break)))

while True:
	answer = input("Do you want to play? Enter y/yes or n/no!")
	if answer not in ('y', 'n', 'yes', 'no'):
		print ("Invalid input.")
		break
		
	if answer == 'y' or answer == 'yes':
		game()
		
	else:
		print ("End game.")
		break

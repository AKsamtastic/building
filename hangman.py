import random

#create a game of hangman

def hangman():
    #computer chooses a random real word from len 3-8.
    #then outputs _ _ _ for len of word.
    while True:
        #print instructions
        print ("Hi cutie, this is a word game, hangman! ")
        print ("The computer has a random word, you must guess letters to figure out the correct answer before you run out of strikes!")
        decision =input("would you like to play? (y/n): \n")
        if decision == "n":
            print ("bye bye!")
        else:
            print ("\nLet's play!")
        #List of word options
        word_options = ["river"]
        #computer gets random word
        word = random.choice(word_options)
        n = sum (c.isalpha() for c in word)
        print ("The computer has a word. ")
        print ("\n",(n * "_ "),"\n")
        
        
        #need to get word_guessed Victory function to work
        #need to position correct letter guesses into the correct location of the word

        while True:
            guess_right = []
            guess_wrong = []
            strikes = 0
            word_guessed = False
            for i in range (0, n):
                if word == guess_right:
                    word_guessed == True
                guess = input("guess a letter: \n")
                if guess in word:
                    guess_right.append(guess)
                    print ("\nyes!")
                    #need to add letter to _ _ _ 
                    print ("\n", f"Here are your correct guesses: {guess_right}")
                    print ("\n The computer's word:", (n * " _"), "\n")
                else:
                    strikes += 1 
                    if strikes < 5:
                        print ("\nnope!", f"You have {5 - strikes} strikes left.")
                        guess_wrong.append(guess)
                        print (f"Here are your wrong guesses: {guess_wrong}")
                    else:
                        print ("\n Sorry, out of guesses!")
            if word_guessed == True:
                print ("You win!")        
                         

hangman ()
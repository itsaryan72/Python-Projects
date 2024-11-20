import random
#,"programming","data","computer","cloud"

def hangman():

    words = ["python","algorithm"]
    word = random.choice(words).lower()
    attempts = 6
    guessed_word = ['_']*len(word)
    guessed_letter = []

    print("Welcome to Hangman!")
    print("You have to guess the word one letter at time.")
    print(f"The word has {len(word)} letters.")
    print(" ".join(guessed_word))

    while attempts > 0 and '_' in guessed_word:
        print(f"\nRemaning attempts: {attempts}")
        guess = input("Enter letter:") 

        if len(guess) != 1 or not guess.isalpha():
            print("Please guess a single letter")
            continue
            
        if guess in guessed_letter:
            print("You already guessed that letter. Try another one")
            continue

        guessed_letter.append(guess)

        if guess in word:
            print(f"Good job! '{guess}' is in the word.")
            for i,letter in enumerate(word):
                if letter == guess:
                    guessed_word[i] = guess
        
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            attempts -= 1

        print(" ".join(guessed_word))


    if "_" not in guessed_word:
        print("\nCongratulations! You've guessed the word:",word)
    else:
        print("\nGame over! The word was:",word)
    

hangman()
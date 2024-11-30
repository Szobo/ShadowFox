import random


def draw_hangman(incorrect_attempts):

    hangman = {
        0: ("   ",
            "   ",
            "   "),
        1: (" o ",
            "   ",
            "   "),
        2: (" o ",
            " | ",
            "   "),
        3: (" o ",
            "/| ",
            "   "),
        4: (" o ",
            "/|\\",
            "   "),
        5: (" o ",
            "/|\\",
            "/  "),
        6: (" o ",
            "/|\\",
            "/ \\")
    
    }

    for line in hangman[incorrect_attempts]:
        print(line)

def play():
    words = ('mango', 'orange', 'apple', 'strawberry', 'banana')
    word_to_guess = random.choice(words)
    guessed_letters = []
    incorrect_attempts = 0
    max_attempts = 6

    print("Welcome to hangman. You are here to die! \n Guess the word letter by letter")

    while incorrect_attempts < max_attempts:
        draw_hangman(incorrect_attempts)
        

        display_word = ""
        for letter in word_to_guess:
            if letter in guessed_letters:
                display_word += letter

            else:
                display_word += "_"
                
        print("Word: ", display_word)

        # Check if the player has guessed the word
        if "_" not in display_word:
            print("Congrats! You've won the game!")
            return
        

        guess = input("Guess a letter my little boy: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Try again my boy.")
            continue


        if guess in guessed_letters:
            print("You already guessed that letter.")

        elif guess in word_to_guess:
            guessed_letters.append(guess)  
            print("You guessed it right") 

        else:
            guessed_letters.append(guess) 
            incorrect_attempts += 1
            print("Poor soul. You will die!")


    word_guessed = True

    for word in guessed_letters:
        if word not in word_to_guess:
            word_guessed = False

            break


    if word_guessed:
        print("Congrats! You've won the game!")

    else:
        draw_hangman(incorrect_attempts)
        print("You lost the game! The correct word was ", word_to_guess)


play()


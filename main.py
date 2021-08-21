import random
choice = ""
print("H A N G M A N")
print("The game will be available soon.")
while choice != "exit":
    word = ('python', 'java', 'kotlin', 'javascript')

    random_word = random.choice(word)
    first_three = random_word[0:3]
    the_rest = random_word[3:]
    first_three_hash = first_three.replace(first_three, "-" * len(first_three))
    the_rest_hash = the_rest.replace(the_rest, "-" * len(the_rest))
    text = first_three + the_rest_hash
    text_2 = (first_three_hash + the_rest_hash)


    trial = 8
    random_word = (random_word)
    guesses = set()

    player_1 = input("Type \"play\" to play the game, \"exit\" to quit: ")
    if player_1 == "play":
        for x in range(trial):
                while text_2 != random_word and trial != 0:
                             print()
                             print(text_2)
                             guess = input("Input a letter: ")
                             if len(guess) == 1:
                                 if  guess.isalpha() and guess.islower() is True:
                                     if guess not in guesses:
                                         guesses.add(guess)
                                         if guess in random_word:
                                             if guess in text_2:
                                                 trial -= 1
                                                 print("No improvements")
                                             indices = []
                                             for i in range(len(random_word)):
                                                 if random_word[i] == guess:
                                                     indices.append(i)
                                                 trip = (random_word.index(guess))
                                                 for trip in indices:
                                                     text_2 = text_2[:trip] + guess + text_2[trip + 1:]

                                         else:
                                             print("That letter doesn't appear in the word")
                                             trial -= 1
                                     else:
                                         print("You've already guessed this letter")
                                 else:
                                     print("Please enter a lowercase English letter")
                             else:
                                 print("You should input a single letter")
                break



        if text_2 == random_word:
                                print()
                                print(text_2)
                                print("You guessed the word!")
                                print("You survived!")
                                print()
        else:
                                print("You lost!")
                                print()

    else:
        print("Thanks for playing!")
        print("We'll see how well you did in the next stage")
        exit()
else:
    exit()



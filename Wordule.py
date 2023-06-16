import random
lives =5

#create a list of secret words
words=['share','shirt','earth','chart','curve','crowd']

#use the choice function of the random module to select a random word from the list
secret_word=random.choice(words)

#create another list to store the clues
clue=list('?????')
heart_symbol= u'\u2764'

guessed_word_correctly = False

# a function to update the clue list
def update_clue(guessed_letter,secret_word,clue):
    index=0
    while index < len(secret_word):
        if guessed_letter ==secret_word[index]:
            clue[index]=guessed_letter
            index +=1

# ask for user input to guess the letter or the word

while lives > 0:
    print(clue)
    print('you have' +str(heart_symbol * lives) + 'lives remaining')
    guess=input('Guess a letter or the whole word:')

    if guess == secret_word:
        guessed_word_correctly=True
        break

    if guess in secret_word:
        update_clue(guess,secret_word,clue)
    else:
        print('Sorry,that letter is not in the word. You lost a life')
        lives-=1

#check if the player has won or lost
if guessed_word_correctly:
    print('You guessed the word! You win!'+ secret_word)
else:
    print('Sorry, you lost. The word was'+ secret_word)



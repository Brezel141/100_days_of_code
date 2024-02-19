
This Python script is a simple implementation of the game Hangman.

The game starts by selecting a random word from a list of words (word_list.word_list). 
It then creates a display list with underscores representing each letter in the chosen word. 
The number of lives the player has is set to 6.

The game loop continues as long as there are still underscores in the display (meaning the word 
has not been fully guessed) and the player still has lives left. In each iteration of the loop, 
the player is asked to guess a letter.

If the guessed letter is in the chosen word, the corresponding underscore(s) in the display is 
replaced with the guessed letter. If the guessed letter is not in the chosen word, the player 
loses a life.

After each guess, the current state of the hangman and the current state of the word (with guessed 
letters revealed and unguessed letters still as underscores) are printed out, along with the number 
of lives remaining.

If the player runs out of lives before guessing the word, a game over message is printed along 
with the correct word.
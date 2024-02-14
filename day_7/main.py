# Hangman

import random
import word_list
import art

chosen_word = random.choice(word_list.word_list)
display = ['_' for _ in chosen_word]
word_lenght = len(chosen_word)
lives = 6

print(art.logo)
print(chosen_word)

while '_' in display and lives > 0 :
  user_input = input("Guess a letter: ").lower()
  
  for position in range(word_lenght):
    letter = chosen_word[position]
    if letter == user_input:
      display[position] = letter
      print(art.stages[lives])
      
  if user_input not in chosen_word:
    lives -=  1 
    print(art.stages[lives])

  print(*display)
  print(f'U have: {lives} Lives')

  if lives == 0:
    print(art.stages[0])
    print(f'Game Over! The word was {chosen_word}')
  
import random
from word import words #imported words from word file
import string  #for ' '.join and string.ascii_uppercase
''' '.join() joins the string list 
    example: ['s', 'a', 'v', 'n'] = savn
'''

#getting valid word(without - and space) from word file
def valid_words():
  word = random.choice(words)

  while ' ' in words or '-' in words:
    word = random.choice(words)
  
  return word.upper()


def hangman():
  rand_word = valid_words()  # all valid words 
  word_letter = set(rand_word)
  alphabets = set(string.ascii_uppercase)
  used_letter = set()
  #print(rand_word) 

  lives = 5
  # play until guessed more than 5 wrong letters
  while len(word_letter) > 0 and lives > 0:
    if len(used_letter) == 0:
      print("used letters: None")
    else:
      print("used letters ", ' '.join(used_letter))
  
    word_list = [letter if letter in used_letter else \
    '_' for letter in rand_word]  ## returns '_ _ _ _ _' if no used letter
    print("current_word = ", " ".join(word_list)) 

    user_input = input("enter your guess letter: ")
    if user_input in alphabets - used_letter:
      used_letter.add(user_input)
      
      if user_input in word_letter:
        word_letter.remove(user_input)

      else:
        lives -= 1
        print("Try different letter.")

    else:
      print("You already guessed this letter.")

  if len(word_letter) == 0:
    print("You Won! The word was " + rand_word)
  else:
    print("you lost! Try again.")

hangman()
  

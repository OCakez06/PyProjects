import random
import pprint
import time


word_categories = {
    "fruits": ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon"],
    "animals": ["elephant", "giraffe", "zebra", "lion", "tiger", "bear", "monkey"],
    "countries":["canada", "brazil", "france", "germany", "india", "japan", "nigeria"],
    "colors": ["red", "blue", "green", "yellow", "orange", "purple", "violet"]}



print("\n".join("{}\t{}".format(k, v) for k, v in word_categories.items()))
choice=0
while choice ==0:
 choice = int(input("which category would you like to choose.Please make a choice\n" + "1 for fruits\n" + "2 for animals\n" + "3 for countries\n" + '4 for colours\n' ))
 if choice !=0:
       break



if choice == 1:
    choice = "fruits"
    play_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon"]
elif choice == 2:
    choice = "animals"
    play_list =  ["elephant", "giraffe", "zebra", "lion", "tiger", "bear", "monkey"]
elif choice == 3:
    choice = "countries"
    play_list = ["canada", "brazil", "france", "germany", "india", "japan", "nigeria"]
elif choice == 4:
    choice= "colours"
    play_list = ["red", "blue", "green", "yellow", "orange", "purple", "violet"]
    
    
wordlooking4 = random.choice(play_list)
print(f"FOR TESTING PURPOSES THE WORD IS {wordlooking4}")
emptylist = []

for i in wordlooking4:
    emptylist += "_"
    
print(emptylist)
newlist = []
print("The game now begins in..")
for i in range(5,0,-1):
    print(i)
    time.sleep(1)
    
guesses = 0
print("you get 7 guesses")
done = False

#FUNCTIONS SECTION!!!!!!!!!!!!!!!!!!!!!!!!!
def wholeword(guessedletter2,wordlooking4,lista2,emptylist): 
    letterslist= list(wordlooking4)
    for i in range(-1,guessedletter2):
        if letterslist[i] == lista2[i]:
            emptylist[i] =letterslist[i]
    print(emptylist)



hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]







































while done == False:
    
    guessedletter = input("Make ur guess\n")
    
    
    
    
    if len(guessedletter) > 1:
      if guessedletter.lower() == wordlooking4.lower():
        emptylist = list(wordlooking4)
        print(emptylist)
        print(f"YOOO you guessed the whole word correctly! It was {wordlooking4}")
        print("you won.")
        exit()
      else:
        guesses = guesses + 1
        print(f"Nah that's not it, you lose a guess!")
        if guesses == 7:
            print(hangman_stages[6])
        else:
            print(hangman_stages[guesses])
        print(f"you got {7-guesses} left")
        if guesses == 7:
            done = True
        continue
    
    lista2= list(guessedletter)
    guessedletter2 = (len(guessedletter))
    
    if guessedletter2>1:
        wholeword(guessedletter2,wordlooking4,lista2,emptylist)
        
        
    
   
        
    
    
    
    for pos in range(len(wordlooking4)):
          letter = wordlooking4[pos]
          if letter == guessedletter.lower():
              emptylist[pos]= letter
              print(emptylist)
              
    if "_" not in emptylist:
        break
              
    if guessedletter not in wordlooking4:
        guesses = guesses + 1
        if guesses == 7:
         print(hangman_stages[6])
        else:
            print(hangman_stages[guesses])
        
    print(f"you got {7-guesses} left")
        
    if guesses == 7:
        done = True

if "_" not in emptylist and guesses <= 7:
    print(f"you actually guess it, it truly was the word {wordlooking4}\n" + "you won.")
    exit()
else:
    print("unlucky.. you truly are like pixie, try again never give up!")
              
 
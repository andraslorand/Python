# this is a hangman game

import random

words=['apple','holocaust','python','game','hangman','house plant','pixelart','old school','hacker']
guessed=False
lifes=5

randomWord=words[random.randint(0,len(words))-1]

def convert(string):
    """this will take the word appart and put the letters into a list"""
    list1=[]
    list1[:0]=string
    return list1

def display():
    """this will display the list acording the guessed words"""
    for element in listToGuess:
        if element in rightGuesses:
            print(element , end=' ')
        else:
            print('_' , end=' ')

def wrongDisplay():
    """these are the wron guesses"""
    print('these are your failures',end='   ')
    for elements in wronGuesses:
        print(elements,end=' ')


listToGuess=convert(randomWord)
rightGuesses=[]
wronGuesses=[]
print(listToGuess)
rguesses=0
while lifes>=0:
    display()
    wrongDisplay()
    print(lifes)
    user_input = input('Enter Your Characters\n')
    if user_input in rightGuesses or user_input in wronGuesses:
        print('try again with a new character, you alreadyu  tried this one')
    else:
        if user_input in listToGuess:
            rightGuesses.append(user_input)
            rguesses+=listToGuess.count(user_input)
            print(rguesses)

            if(rguesses==len(words)):
                break

        else:
            wronGuesses.append(user_input)
            lifes-=1
    
    
    
    


if lifes<=0:
    print('you are a looser')
else:
    print('you are a winner')
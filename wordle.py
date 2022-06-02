# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 21:01:31 2022

@author: foster boone
"""

import random as random

main_dict=[]
final_dict=[]
cleaned_dict=[]   
with open("./dictionary.txt", "r") as dictionary:
    for line in dictionary:
        data = line.split()
        main_dict.append(data)
for i in main_dict:
    for x in i:
        final_dict.append(x)       
for word in final_dict:
    
    if len(word)==5:
        cleaned_dict.append(word)
alphabet=["a","b","c","e","f","g","h","i","j","k","l","m",
          "n","o","p","q","r","s","t","u","v","w","x","y","z"]


def containsUpper(string):
    for letter in string:
        if letter.isupper():
            return True
        return False
def isInList(theWord,theList):
    if theWord in theList:
        return True
    return False
def strToList(string):
    new_list=[]
    for letter in string:
        new_list.append(letter)
    return new_list    
def wordle(wordToGuess):
    n=0
    greenLetters=[]
    yellowLetters=[]
    grayLetters=[]
    while n<6:
        #This portion is to make sure the word is viable
        guess=input("Make a guess!")
        while len(guess)!=5 or containsUpper(guess):
            if len(guess)!=5:
                guess=input("That word is not five letters")
            if containsUpper(guess):
                guess=input("That word contains an upper case letter")
        while isInList(guess,cleaned_dict)==False:
            guess=input("That is not a word")
        #this portion is to compare the words
        checkWord=[]
        checkWin=0
        previousLetters=[]
        for guessLetter in guess:           
            isLetter=False
            isPosition=False
            for wordLetter in wordToGuess:
                if guessLetter==wordLetter:
                    isLetter=True        
                    if strToList(guess).index(guessLetter)==strToList(wordToGuess).index(wordLetter):
                        isPosition=True
            if isInList(guessLetter,alphabet):
                alphabet.pop(alphabet.index(guessLetter))
            if isLetter:                
                if isPosition:
                    checkWord.append("{"+guessLetter+"}")
                    if isInList(guessLetter, greenLetters)==False:
                        greenLetters.append(guessLetter)
                    checkWin+=1
                if isPosition==False:
                    if isInList(guessLetter,previousLetters)==False:
                        checkWord.append("["+guessLetter+"]")
                        if isInList(guessLetter, yellowLetters)==False:
                            yellowLetters.append(guessLetter)
                    if isInList(guessLetter,previousLetters):
                        checkWord.append("("+guessLetter+")")
            else:
                checkWord.append("("+guessLetter+")")
                if isInList(guessLetter, grayLetters)==False:    
                    grayLetters.append(guessLetter)
            previousLetters.append(guessLetter)
        print(checkWord)
        
        if checkWin==5:
            return print("You won!")
            
        n+=1
    return print("Sorry, you lost! " +"The word is "+"'"+wordToGuess+"'")

def randomFromList(theList):
    n=random.randint(0,len(theList))
    return theList[n]

wordle(randomFromList(cleaned_dict))

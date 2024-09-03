import math
import random

#easy or hard mode
while True:
    gMode = input("\neasy or hard mode? ")
    if gMode == 'easy' or gMode == 'hard' or gMode == 'idiot':
        break
    else:
        print("idiot. type in 'easy' or 'hard' \n")

#choosing the inputs for upper boudns; also has failsafe for hitansh cases
while True:
    try:
        input1 = input("Choose the Upper Bound:- ")
        upper = int(input1)
        break
    except:
        print('I meant an integer idiot\n')     

#choosing the lower bound
while True:
    try:
        input2 = input("Choose the Lower Bound:- ")
        lower = int(input2)
        if lower != upper:
            break
        else:
            print('you need two different numbers\n')
        
    except:
        print('I meant an integer idiot\n')


#extra hitansh proofing
if lower> upper:
    print('you actual idiot, lower means less than\n\t0_0\n')
    exit()




#finding the correct number and number of guesses, and other ranges
cNum=random.randint(lower,upper)

#creates guess max based on game difficulty
if gMode == 'hard':
    maxGuess = math.ceil(math.log(((upper-lower)/2)+15)+((upper-lower)//50))
elif gMode == 'easy':
    maxGuess = math.ceil((upper-lower)/2)
elif gMode =='idiot':
    maxGuess = upper-lower

#in case of really small range
if upper-lower<=8 and gMode =='hard':
    maxGuess = 1


closeRange = math.ceil((upper-lower)/20)
farRange = math.ceil((upper-lower)/5)

print('\n\n\tCool Beans!\nyou have ', maxGuess, ' attempts to guess the number\n')


#instantiate guesses
guessCount = 0
correct = False
input3 = 0

#runs the commands for the user to actually guess 
while guessCount < maxGuess:
    while True:
        #makes sure guess is an integer and gets guess input
        try:
            input3 = input('\n___________________\nWhat do you think the number is:- ')
            guess = int(input3)
            break
        except: 
            print('HITANSH, USE AN INTEGER\n\n')
    guessCount+=1

    #case1, user gets it right, ends game and congratulates
    if guess == cNum:
        print('\n********************\nCongrats, you got it in ', guessCount, ' tries,' )
        if guessCount <= (maxGuess/2):
            print ('WOW! You still had half the guesses left')
        correct = True
        break

    #case2 user guesses too big, tells them, then gives hint if applicable
    elif guess > cNum:
        print ('To big!')
        if guess<(cNum+closeRange):
            print('you were close though!')
        elif guess>(cNum+farRange):
            print("And you were waaay off too!")
    
    #case3 user guesses too small, tells them, gives hint if applicable
    elif guess < cNum:
        print ('To Small!')
        if guess>(cNum-closeRange):
            print('you were close though!')
        elif guess<(cNum-farRange):
            print("And you were waaay off too!")

#case4, user never gets it right, tells them, shames them, explains correct answer
if not correct:
    print("\n********************\nwow...\nyou're not very good at this")
    print("the correct answer was ", cNum)









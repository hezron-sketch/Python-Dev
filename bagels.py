# Bagels python game
import random

num_digits = 3 #try setting this to 1 or 10
max_guess = 10 #try setting this to 1 or 100

def main():
    print("""Bagels game. Am thinking of a number with no repeated digits. Try guess what it is...
          Here are clues:
          When I say:       What it means
          pico              one digit is correct in the wrong position
          fermi             one digit is correct in the right position
          bagels            no digit is correct no right position""")
    while True: #main game loop
        #store secret number player needs to guess
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print('You have {} guesses to get it.'.format(max_guess))
        
        numGuesses = 1
        while numGuesses <= max_guess:
            guess = ''
            #keep loopin until they get a valid guess
            while len(guess) != num_digits or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')
                if len(guess) == 3:
                    pass
                else:
                    print('That is not a valid number. Try again.')
                
                
            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1
            
            if guess == secretNum:
                break #They are correct so break out of this loop
            if numGuesses > max_guess:
                print('You have run out of guesses. The number was {}'.format(secretNum))
                break
        
        #Ask player if they want to play again
        print('Do you want to play again? (y/n):')
        if not input('> ').lower().startswith('y'):
            break
    print('Thanks for playing')
    
def getSecretNum():
    """Returns a string made up of num_digits unique random digits."""
    numbers = list('0123456789') #ceate a list of digits 0 to 9
    random.shuffle(numbers) #shuffle numbers into a random order
    
    #get the first num_digits in the list for the secret number:
    secretNum = ''
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a list of clues for the given guess and secret number."""
    if guess == secretNum:
        return ['You are correct!']
    
    clues = []
    
    for i in range(len(guess)):
        if guess[i] == secretNum[1]:
            clues.append('fermi') #correct digit in the correct place
        elif guess[i] in secretNum:
            clues.append('pico') #correct digit incorrect place
    if len(clues) == 0:
        return 'Bagels' #incorrect digit incorrect place
    else:
        #sort clues into alphabetic order so that they dont give away information
        clues.sort()
        # make a single string from the list of string clues
        return ''.join(clues)

# if the program is run (instead of importing), run the game
if __name__ == '__main__':
    main()
    
########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
#import modules needed
import random 
def play_again(z) -> bool:
    while True:
        play = input('Do you want to play agin?\n')
        play = play.upper()
        if (play == 'Y') or (play == 'YES'):
            return z == True
            break
        elif (play == 'N') or (play == 'NO'):
            return z == False
            break
        print('You must enter Y/N/YES/NO to continue')
    ''' Asks the user if they want to play again, returns False if N or NO, and 
True if Y or YES.  Keeps asking until they respond yes '''
    return True
     
def get_wager(bank : int) -> int:
    while True:
        wager = int(input('How many chips do you want to wager?'))
        if wager < 0:
            print('Wager has to be greater than zero')
        
        if wager > bank:
            print('Wager cannot be bigger than bank')
            wager = bank
        else:
            return wager 
            
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is 
<= 0 or greater than the amount they have '''
    return 1            
def get_slot_results() -> tuple:
    numA = random.randint(1,10)
    numB = random.randint(1,10)
    numC = random.randint(1,10)
    return(numA,numB,numC)
    
    
    ''' Returns the result of the slot pull '''
    return 1, 2, 3
def get_matches(reela, reelb, reelc) -> int:
    if (reela == reelb) and (reela == reelc):
        return 3
    if (reela == reelb) or (reela == reelc) or (reelb == reelc):
        return 2
    
                            
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    return 0
def get_bank() -> int:
    while True:
        chips = int(input('How many chips do you want to start with?'))
        if (chips > 0) and (chips < 101):
            return chips
        if chips < 0:
            print('Too low a value, you can only choose 1 - 100 chips')
        if chips > 101:
            print('Too high a value, you can only choose 1 - 100 chips')
        
        
    ''' Returns how many chips the user wants to play with.  Loops until a value 
greater than 0 and less than 101 '''
    return 0
def get_payout(wager, matches):
    if matches == 3:
        return wager*10
    if matches == 2:
        return wager*3
    
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times 
the wager if 2 match, and negative wager if 0 match '''
    return wager * -1     
if __name__ == "__main__":
    playing = True
    while playing:
        bank = get_bank()
        initialbank = bank
        count = 0
        newbank = 0
        newhigh = bank 
        while bank > 0:
            
            wager = get_wager(bank)
            reel1, reel2, reel3 = get_slot_results()
            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout
            if bank > newbank:
                newhigh = bank
            newbank = bank
            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            count += 1
        print("You lost all {} in {} spins".format(initialbank,count))
        print("The most chips you had was {}".format(newhigh))
        playing = play_again(playing)

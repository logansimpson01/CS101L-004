print('Welcome to the Flarsheim Guesser!')
choice = 'y'


while(choice == "Y" or choice == "y"):
# I want the yes choice to be repeated
    print('\nPlease think of a number between and including 1 and 100.')
    three_remainder = 0
    five_remainder = 0
    seven_remainder = 0
    #set values
    three_remainder = int(input('What is the remainder when your number is divided by 3 ?\n'))
    while (three_remainder<0 or three_remainder>=3):            
        if three_remainder<0:
            print('The value entered must be 0 or greater')
        elif three_remainder>=3:
            print('The value entered must be less than 3')

        three_remainder = int(input('What is the remainder when your number is divided by 3 ?\n'))

# if i has a three remainder then loop same for other remainders
    five_remainder = int(input('What is the remainder when your number is divided by  5 ?\n'))
    while (five_remainder<0 or five_remainder>=5):            
        if five_remainder<0:
            print('The value entered must be 0 or greater')
        elif five_remainder>=5:
            print('The value entered must be less than 5')

        five_remainder = int(input('What is the remainder when your number is divided by  5 ?\n'))

    seven_remainder = int(input('What is the remainder when your number is divided by  5 ?\n'))
    while (seven_remainder<0 or seven_remainder>=5):            
        if seven_remainder<0:
            print('The value entered must be 0 or greater')
        elif seven_remainder>=5:
            print('The value entered must be less than 5')

        seven_remainder = int(input('What is the remainder when your number is divided by  7 ?\n'))

# divide and find remainders 
    for i in range(1,101):
        if(i%3 == three_remainder and i%5 == five_remainder and i%7 == seven_remainder):
            print('Your number was', i)
            print('How amazing is that?\n')
# ask user to play again
    choice = input('Do you want to play again? Y to continue, N to quit  ==>')
    while (choice != 'Y' and choice != 'y' and choice!= 'N' and choice!= 'n'):
        choice = input('Do you want to play again? Y to continue, N to quit  ==>')
        

    
    
        


    

    
        

              
    
          




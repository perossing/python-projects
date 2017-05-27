# Python 2.7.13
# author: Peter Rossing
# Tech Academy - Python Course, Basics Drill (Item 36)


# ===== ASSIGNMENT CRITERIA NOTED THROUGHOUT CODE =====

import time

def start():
    # --- Assign an integer to a variable ---
    x = 10
    # --- Assign a float to a variable ---
    y = 3.14
    # --- Assign a string to a variable ---
    sentence = 'Once upon a midnight dreary'

    userEntry = ''

    # --- Use print function and .format() to print variables ---
    print '\n\nHello, welcome to my first Python program!'
    print '\nSo far, I\'ve assigned values to three variables, "x", "y", and "sentence": \n\n\tx equals {}, \n\ty equals {}, \n\tsentence is "{}".'.format(x,y,sentence)
    print '\nNow let\'s use these variables...'

    # --- Use a while loop ---
    while userEntry == '':

        userEntry = raw_input('Please enter a whole number between 1 and 5: ')

        try:
            userNumber = int(userEntry)

    # --- Use conditional statements if, elif, else ---
    # --- Use logical operators and, or (not is below) ---
            if userNumber > 0 and userNumber < 6:
                print('\nNow we\'ll use your number to do some things with our variables!')
            else:
                userNumber < 1 or userNumber > 5
                print('\nThat number is not between 1 and 5...')
                userEntry = ''
        except:
            print('\nYour entry is not whole number...')
            userEntry = ''

    useVariables(userNumber,x,y,sentence)


def useVariables(userNumber,x,y,sentence):
    # --- Use operators +,- ---
    print '\nYou\'re number is {}:'.format(userNumber)
    time.sleep(1)
    print '\t{} times x equals '.format(userNumber) + str(x * userNumber)
    time.sleep(1)
    print '\t{} plus y equals '.format(userNumber) + str(y + userNumber)
    time.sleep(1)
    print '\t100 divided by x, minus {} equals '.format(userNumber) + str( 100/10 - userNumber)
    time.sleep(1)
    print '\tThe number of characters in our sentence variable (' + str(len(sentence)) + '), divided by your number leaves a remainder of ' + str(len(sentence) % userNumber) + '.'

    time.sleep(2.5)
    print '\nAnd now for something completely different! A list of 19th-Century American Poets:\n'
    listPoets(userNumber)


def listPoets(userNumber):
    # --- Create list and iterate through to print each line ---   
    myList = ['Stephen Crane', 'Emily Dickinson', 'Ralph Waldo Emerson', 'Edgar Allen Poe', 'Walt Whitman']
    # --- Use a for loop --- 
    time.sleep(2)
    for poets in myList:
        print '\t' + poets
    index = userNumber
    index -= 1
    time.sleep(0.5)
    print '\n\tThe name in the list that corresponds to your number is:\n\t' + myList[index] + '.'
    
    time.sleep(3)
    loopTuple(userNumber)
    

def loopTuple(userNumber):
     # --- Create a tuple and iterate through to print each line ---   
    myTuple = ('math', 'poets', 'variables', 'Python', 'console')

    time.sleep(1)
    print '\nWe\'re almost done!'

    # --- Use logical operator not (and and or are above) ---
    if not (userNumber == 1):
        print 'Since your number is {}, here are {} things we learned about today:'.format(userNumber,userNumber)
    else:
        print 'Since your number is {}, here is {} thing we learned about today:'.format(userNumber,userNumber)

    counter = 0
    for counter in range (0,userNumber):
        print '\t' + myTuple[counter]
        counter += 1

    strQuestion()

     
def strQuestion():
    stop = False
    print('\nBefore we finish...')
    while stop == False:
        choice = raw_input('Would you like to know where the text of the "sentence" variable comes from? y/n: ').lower()
        if choice == 'y':
            # --- Call the function that returns a string variable and print result to shell ---   
            print(showRaven())
            stop = True
        elif choice == 'n':
            print('\nOK, thanks for looking at my Python program!\n')
            stop = True
            exit()
        else:
            print('\nPlease enter \'y\' for YES and \'n\' for NO...')


def showRaven():
     # --- Define a function that returns a string variable ---   
    theRaven = ('\nThe text is the first line of "The Raven," by Edgar Allen Poe. \n--Goodbye! \n')
    return theRaven









if __name__ == "__main__":
    start()

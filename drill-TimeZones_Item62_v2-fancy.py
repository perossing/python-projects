# Python 2.7.13
# Peter Rossing, 06/02/2017
# Tech Academy Drill (#Item 62)



import time
import datetime

def start():
    
    #for testing...
    #portlandTime = '21:08'
    
    portlandTime = datetime.datetime.now().strftime('%H:%M')
    portlandHour = int(portlandTime[0:2]) # slices first two digits from string and converts to integer
    minutes = portlandTime[3:5] # slices last two digits from string. keep in str format to concatenate later
    
    class newYork():
        branch = 'New York'
        hour = portlandHour+3        

    class london():
        branch = 'London'
        hour = portlandHour+8

    
    ask = True
    while ask == True:
        
        city = raw_input('\nWhich branch\'s hours would you like to check?: (New York/London) ').lower()

        if city == 'new york' or city == 'london':
            ask = False

            if city == 'new york':
                city = newYork
            else:
                city = london

            printInfo(city, minutes, portlandHour)

        else:
            print 'Please enter either New York or London...'


def convertTime(cityhours, minutes):  # converts 24-hour time to 12-hour time and adds A.M. or P.M.
    
    am_pm = 'A.M.'

    if cityhours > 11 and cityhours < 24:
        am_pm = 'P.M.'

    if cityhours > 24:
        cityhours -= 24  # numbers 25 & up get reset to 1 & up       
   
    #hour12 = cityhours
    
    if cityhours > 12:
        cityhours -= 12   

    return str(cityhours) + ':' + minutes + ' ' + am_pm


def printInfo(city, minutes, portlandHour):

    cityhours = city.hour

    fullTime = convertTime(cityhours,minutes)
    portlandFull = convertTime(portlandHour, minutes)
    
    open_closed = 'OPEN' 
    if (city.hour < 9 or city.hour > 21):
        open_closed = 'CLOSED'

    print '\nThe time in Portland is: ' + portlandFull
    print 'The time in ' + city.branch + ' is: ' + fullTime + ' The branch is ' + open_closed + '.\n'

    checkAgain()    
            

def checkAgain():
        stop = False
        
        while stop == False:
            again = raw_input('Would you like to check another branch\'s hours?: (Y/N) ').lower()
           
            if again == 'y':
                stop = True
                start()
            elif again == 'n':
                print '\nThank you!'
                stop = True
            else:
                print 'please enter Y or N'



if __name__ == "__main__":
    start()


        
    










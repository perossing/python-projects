# Python 2.7.13
# Peter Rossing, 06/02/2017
# Tech Academy Drill (#Item 62)


import time
import datetime

portlandTime = datetime.datetime.now().strftime('%H:%M')

# for testing...
# portlandTime = '24:08'

portlandHour = int(portlandTime[0:2])
minutes = portlandTime[3:5]


nyHours = portlandHour+3
if nyHours > 24:
    nyHours -= 24
    
londonHours = portlandHour+8
if londonHours > 24:
    londonHours -= 24

nyOpen = 'OPEN' 
if (nyHours < 9 or nyHours > 21):
    nyOpen = 'CLOSED'

londonOpen = 'OPEN' 
if (londonHours < 9 or londonHours > 21):
    londonOpen = 'CLOSED'    

print 'The time in Portland is: ' + str(portlandTime)+'.'
print 'The time in New York is: ' + str(nyHours)+':'+ minutes +'. The branch is ' + nyOpen + '.'
print 'The time in London is: ' + str(londonHours)+':'+ minutes +'. The branch is ' + londonOpen + '.'

        
    










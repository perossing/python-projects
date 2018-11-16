import datetime, time
#from tkinter import *



##currentUnix = time.time()
##print(currentUnix)
##print(datetime.datetime.fromtimestamp(int(currentUnix)).strftime('%Y-%m-%d %H:%M:%S'))
##
##print(datetime.datetime.fromtimestamp(int(currentUnix)).strftime('%Y-%m-%d, %H:%M:%S'))
date = (datetime.datetime.fromtimestamp(int(time.time())).strftime('%m/%d/%Y'))
time = (datetime.datetime.fromtimestamp(int(time.time())).strftime('%H:%M:%S'))
print(date)
print(time)

##monkey = (datetime.datetime.fromtimestamp(int(currentUnix)).strftime('%Y-%m-%d, %H:%M:%S'))
##print (monkey)
##print (type(monkey))

##dayAgo = currentUnix - 86400
##print(dayAgo)
##print(datetime.datetime.fromtimestamp(int(dayAgo)).strftime('%Y-%m-%d %H:%M:%S'))

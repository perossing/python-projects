# tech-academy_python-drills


I)
 (item #36) Basic concepts -- Write a program in Python 2.7 using IDLE that demonstrates the following. (Use comments in your program to denote where you demonstrate each step): 

1. Assign an integer to a variable
2. Assign a string to a variable
3. Assign a float to a variable
4. Use the print function and .format() notation to print out the variable you assigned
5. Use each of these operators +, - , * , / , +=, ­= , %
6. Use of logical operators: and, or, not
7. Use of conditional statements: if, elif, else
8. Use of a while loop
9. Use of a for loop
10. Create a list and iterate through that list using a for loop to print each item out on a new line
11. Create a tuple and iterate through it using a for loop to print each item out on a new line
12. Define a function that returns a string variable
13. Call the function you defined above and print the result to the shell


II) (item #46) Range function:

1. Use the Python range() function with one parameter to display the
following:

 0

 1

 2

 3

2. Use the Python range() function with 3 parameters to display the following:
3 2 1 0

3. Use the Python range() function with 3 parameters to display the following:
8 6 4 2


III) (item #48) Sorting:

Write your own version of the sorted() method in Python. This method should take a list as an argument and return a list that is sorted in ascending order. Call your method passing in the following lists as arguments and print out each sorted list to the shell. This should be an algorithm that you write. Do not use .sort() or the sorted() methods in your method.

[67, 45, 2, 13, 1, 998]

[89, 23, 33, 45, 10, 12, 45, 45, 45]



IV) (item #62) Convert Time Zones:

Scenario: The company you work for just opened two new branches. One is in New York City, the other in London. They need a very simple program to find out if the branches are open or closed based on the current time of the Headquarters here in Portland. The hours of both branches are 9:00AM - 9:00PM in their own time zone. Create code that will use the current time of the Portland HQ to find out the time in the NYC & London branches, then compare that time with the branches hours to see if they are open or closed.  Print out if each of the two branches are open or closed.

Guidelines:

- Use Python 2.7 IDLE

- Use Datetime Module

- Execute program on the Shell


V) (item #63) File Mover:

Scenario: Your employer wants a program to move all his .txt files from one folder to another
with the click of a click of a button. On your desktop make 2 new folders. Call one Folder A &
the second Folder B. Create 4 random .txt files & put them in Folder A. Plan: Move the files from Folder A to Folder B. Print out each file path that got moved onto the shell. Upon viewing Folder A after the execution, the moved files should not be there.

Guidelines:

- Use Python 2.7 .x on this drill.

- Import the shutil module.

- Run it on the python shell.

- Use the IDLE for this Drill.


VI) (item #64)  Daily File Transfer:
Scenario: Your company's users create or edit a collection of text files throughout the day. Once per day, any files that are new, or that were edited within the previous 24 hours, must be sent to the home office. To facilitate this, these new or updated files need to be copied to a specific 'destination' folder on a computer, so that a special file transfer program can grab them and transfer them to the home office. The process of figuring out which files are new or recently edited, and copying them to the 'destination' folder, is currently being done manually. You have been asked to create a script that will automate this task.

Guidelines:
Use Python 2.x


VII) (item #65) UI for File Transfer project:

Users are asking for a user interface to make using the script easier and more versatile.
Desired features of the UI:

- Allow the user to browse to and choose a specific folder that will contain the
files to be checked daily.

- Allow the user to browse to and choose a specific folder that will receive the
copied files.

- Allow the user to manually initiate the 'file check' process that is performed by
the script.


Guidelines:

- Use Python 3.4 for this drill.

- Use tkinter to create the UI.

- The layout of the UI is up to you.

- You should use IDLE for this Drill. 


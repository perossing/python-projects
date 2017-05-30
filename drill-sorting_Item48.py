# Python 3.6.1
# author: Peter Rossing
# Tech Academy - Python Course, Sorting Drill (Item 48)



'''
===== ABOUT THE CODE =====

The first version is bubble sort with comments about
what's happening in each part of the code

The next version of selection sort includes comments and print statements
to explain what's happening at each stage of the program.

The last version is the selection sort code without comments & print statements

'''


listA = [67, 45, 2, 13, 1, 998]
listB = [89, 23, 33, 45, 10, 12, 45, 45, 45]

# i is index location of the number being sorted


def bubbleSort(list):
    # Start sorting with the number in last position and goes through each index from last to first:
    for numToSort in range(len(list)-1,0,-1):
        for i in range(numToSort):
            
            # Compares the number to sort with the next number in the list:
            # (in the case of last number, the next one is the first number)
            if list[i]>list[i+1]:
                
                # If the number to sort is greater than the next one in the list, swap the two numbers:
                # (the larger number gets moved one position closer to the end)
                list[i], list[i+1] = list[i+1], list[i]


print('\nbubble sort: \n')

bubbleSort(listA)
print(listA)

bubbleSort(listB)
print(listB)



def selectionSort_Annotated(list):  
    # Start sorting with the number in last position and go through each index from last to 1st:
    for numToSort in range(len(list)-1,0,-1):
        # Set the first number in the list as the one to compare the 'sort number' to: 
        print(list)
        compare = 0

        # Before sorting/moving any numbers, look at each number in the list (starting with the 2nd number)
        # and compare it to the 1st number:
        for i in range(1, numToSort+1):
            print('\tis ' + str(list[i]) + ' larger than ' + str(list[compare]) + '?')
            # If one of the numbers in the list is larger than the 1st number...
            if list[i] > list[compare]:
                print('\t\tYes!')
                # ... use that number instead of the 1st number to compare the 'sort number' to:
                compare = i
                print('\tcompare is now at index: ' + str(compare))

        print('Is ' + str(list[compare]) + ' larger than ' + str(list[numToSort]) + '?')
        # If the 'compare number' is larger than the 'sort number'...
        if list[compare] > list[numToSort]:
            # Swap the 'compare number' and the 'sort number':
            # (the larger number ends up in the position of the number being sorted)
            list[numToSort], list[compare] = list[compare], list[numToSort]
            print(str(list[numToSort]) + ' swapped with ' + str(list[compare]))


print('\n\nselection sort: \n')

selectionSort_Annotated(listA)
print(listA)




def selectionSort(list):  
    
    for numToSort in range(len(list)-1,0,-1):
        compare = 0
        for i in range(1, numToSort+1):
            if list[i] > list[compare]:
                compare = i

        if list[compare] > list[numToSort]:
            list[numToSort], list[compare] = list[compare], list[numToSort]


print('\n\nselection sort again: \n')
selectionSort(listA)
print(listA)

selectionSort(listB)
print(listB)
        
        
   


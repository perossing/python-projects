# Python 3.6.1
# author: Peter Rossing
# Tech Academy - Python Course, Range Drill (Item 46)


num_list = [0,1,2,3,4,5,6,7,8]

for num in(range(4)):
    print(num_list[num])
    
num_str = ''
for num in (range(3,-1,-1)):
    num_str += str(num)
print('\n' + num_str)


num_str = ''
for num in (range(8,1,-2)):
    num_str += str(num)
print('\n' + num_str)


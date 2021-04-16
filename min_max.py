#Conor Smith
# Date: 04/14/2021
# Description: Asks user for number of numbers they want to input, asks for that many #'s, gives back the largest and smallest


print("How many integers would you like to enter?") #get total number of integers from user
num_1 = int(input()) #convert user entered number into a variable
print("Please enter", num_1, "integers.")
max = -99999999
min = 99999999
#start for loop that loops for the range between 1 and the user entered number taking an integer input from user each time
for i in range(1, num_1 +1):
    num_2 = int(input())
    if num_2 < min: #if number entered is less than a very large number it becomes user entered #, after first loop will compare one entry to the next
        min = num_2

    if num_1 > max: #same as above but opposite, if user entry is bigger than a very large negative number variable for max is set to user entered number, then next loops compares user entries. Largest number stays
        max = num_2
print("min :", min) #prints results of smallest and largest
print("max :", max)
#obvious flaw is if someone enters number bigger than 99999999

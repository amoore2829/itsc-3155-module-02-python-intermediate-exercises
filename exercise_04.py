#Take in 5 int inputs from the user and add them together. 
#The catch is that you can no longer assume that what the user enters is a valid int. 
#If the user enters an invalid input, print an error message and make the user input the int again until all 5 int values are entered correctly. 
#Print the resulting sum.

#Worked with Bishal, Sudamesh, and Emre

num_list_1 = []
x = 0
while x < 5:
    try:
        val = input(f'Enter an int #{x+1}: ')
        val = int(val)
        num_list_1.append(val)
    except:
        print('Invalid input, please enter an integer.')
        x = x - 1
    x = x + 1

print('Your sum is: ', sum(num_list_1))


        
        


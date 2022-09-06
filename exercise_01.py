#Write a function that takes in a list data structure as input. 
#The function should create a new list and only include unique elements of the inputted list. 
#Under the function, write code that calls the function with a test list like so and print out the result. 
#Remember that your code should work for all lists of integers, not just the sample test here.

my_list = [1, 2, 3, 2, 1, 4]
unique_list = list(set(my_list))
print(unique_list)

#for x in range (6):
    #num = int(input(f'Enter number {x+1}: '))
    #my_list.append(num)

#print ('Nums that appear once: ', unique_list)


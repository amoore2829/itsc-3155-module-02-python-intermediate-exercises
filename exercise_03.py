#Take in a string from the user and pass it as input to a function. 
#Have the function return a dict which keeps count of each letter (in lowercase) in the string, excluding spaces. 
#Print out this dict.

#Worked with Bishal, Sudamesh and Emre


from itertools import count


val = input("Enter a string: ")


def count_letters(string):
    my_dict = {}
    for letters in string:
        if(letters != " "):
            my_dict[letters] = string.count(letters)
    return my_dict

print(count_letters(val))


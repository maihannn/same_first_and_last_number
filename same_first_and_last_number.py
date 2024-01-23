# Name: Jamaica C. Palillo
# Section: BSCPE 1-5

# Exercise 5: Check if the first and last number of a list is the same.

# Make a list
# Given:

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

# Checking if the first and last number is the same

def result (list_of_numbers):
    first_number =list_of_numbers [0]
    last_number = list_of_numbers [-1]
    
    if (first_number == last_number):
        return True
    else:
        return False
    

print ("The Given List is: ", numbers_x, "=", result (numbers_x))
print ("The Given List is: ", numbers_y, "=", result (numbers_y))
# This program is a conversion tool
# 17/1/25 - this is a change to the program to test the commit and push feature
# 17/1/25 - this is change #2

# Required steps:
# 1 - modularised functions for conversion formulas, (m to km, celcius to farenheight, miles to km)
# 2 - user input
# 3 - Validate user input to check that the input is in the correct format - could this be done with a global function?
# 4 - Run the formula
# 5 - Display the result
# 6 - ask user if they want to run the calculator again

###
# Step 1, define individual conversion functions.
###

# metres to km
def m_to_km(user_input):
    result = (user_input * 10)
    return result

# Celcius to farenheit
def celcius_to_farenheit(user_input):
    result = (user_input * (9 / 5) + 32)
    return result

# miles to km
def miles_to_km(user_input):
    result = user_input * 1.609
    return result

# Create prompt with input for user to choose which conversion they want to make
#16/1/25 current code works well
conversion_selection = input('Choose the conversion you would like to complete:'
                             '\n>1 - metres to km'
                             '\n>2 - celcius to farenheit'
                             '\n>3 - miles to km\n')

#Get users to input the value they need converted
##TO DO##
# How to account for instances where the user doesn't input an appropriate input
# 16/1/25 - current code works well
user_input = float(input('enter a value to convert'))

# Perform logic on user input (conversion_selection) to call the correct function.
# 16/1/25 - this works well
if conversion_selection == '1':
    print(m_to_km(user_input))
elif conversion_selection == '2':
    print(celcius_to_farenheit(user_input))
else:
    print(miles_to_km(user_input))

rerun_calculator = input('Would you like to complete another calculation?'
                         '\n Y'
                         '\n N \n')

check_list = ['y', 'yes', 'n', 'no']

if rerun_calculator.lower in check_list:
    print('need to write a function to restart the program')
    # 16/4 - This isn't working as it is skipping to the final else statement
else:
    print('thanks for using the calculator')


# Questions / commentss with my code:
# 11/1/24
# are functions separate from eachother? With the  'result' this is repeated within all of the functions, but is it separate, so no error will be generated?
# the individual variables within the functions is a pain and will be annoying to code each one, can I call this variable the same thing, say, 'user inuput' within
# each of the functions and the code will work?
# ANSWER
# Functions are separate from eachother. I capture one user_unput and this is the same input for each of the functions, but it depends which one is called


#### Insights
# the user input, when i called it 'user input' and passed that into the function, that worked
# 16/1/24
# The functions weren't working as intended as the input is a 'str' format so the maths operators weren't working


#### Issues


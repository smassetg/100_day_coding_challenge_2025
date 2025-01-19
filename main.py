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
    result = (user_input / 1000)
    return result

# Celcius to farenheit
def celcius_to_farenheit(user_input):
    result = (user_input * (9 / 5) + 32)
    return result

# miles to km
def miles_to_km(user_input):
    result = user_input * 1.609
    return result

#19/1/25 - these functions don't need to be commented out as they aren't being called

def unit_calculator():
# # Create prompt with input for user to choose which conversion they want to make
# #16/1/25 current code works well
# #19/1/25############################

    while True:
        conversion_selection = input('Choose the conversion you would like to complete:'
                                     '\n>1 - metres to km'
                                     '\n>2 - celcius to farenheit'
                                     '\n>3 - miles to km\n')
        if conversion_selection not in ('1', '2', '3'):
            print('Please enter a value from 1 - 3')
        else:
            break

    # My understanding of the above is that the while loop performs the logic on the user input, and is a way to check if appropriate data is entered
    # to continue the program. This uses an if statement to check the values is a Python tuple.

# Create a check condition to make sure only valid input is recieved for the above list:


#Get users to input the value they need converted
##TO DO##
# How to account for instances where the user doesn't input an appropriate input
# 19/1/25 - see below - the while loop handles this
# 16/1/25 - current code works well
# 19/1/25 - how do I get input from user and convert to float and check validity of input from user. ie only float
# The while loop works correctly as it calls a float, which covers int values also. with testing it seems that non-numerical values
# are handled by the except ValueError, but I don't know why this works really, I did copy this from StackOverflow (https://stackoverflow.com/questions/23294658/asking-the-user-for-input-until-they-give-a-valid-response)

    while True:
        try:
            user_input = float(input('enter a value to convert'))
        except ValueError:
            print("The input entered is invalid")
            continue
        else:
            #The given input was valid and we can exit the loop and continue with the calculation
            break


    # Perform logic on user input (conversion_selection) to call the correct function.
    # 16/1/25 - this works well
    if conversion_selection == '1':
        print(m_to_km(user_input))
    elif conversion_selection == '2':
        print(celcius_to_farenheit(user_input))
    else:
        print(miles_to_km(user_input))

#19/1/25###################

    rerun_calculator = input('Would you like to complete another calculation?'
                             '\n Y'
                             '\n N \n')

    check_list = ['y', 'yes', 'Y']
    #19/1/25 - removed the 'n' values as it is only the yes values we want to rerun the rpogram

    if rerun_calculator in check_list:
        # 16/1 - This isn't working as it is skipping to the final else statement
        # 19/1/25 it was the rerun_calculator.lower that wasn't working
        unit_calculator()  #trying to rerun the function if the user chooses to
    else:
        print('thanks for using the calculator')

    return

# 19/1/25 - call the function to initiate the program


unit_calculator()



# 19/1/25 next tasks
# ask chat about how i can track my code a bit better, or how I can structure things instead of the dated comments that I have
# been putting in.
# Learn about debugging with pycharm, ask chat to set some simple debugging challenges to work on in pycharm
# get chat to review this program and provide guidance on refactoring
# Get chat to use this code to prove my level to set me more developmental tasks
# get advice from chat about if I should add these debugging challenges to another branch on github or how to structure things in github
# then - look to do some read/write with .txt document to create a litte database program
# then think how i could build on this to create my fast mental maths program

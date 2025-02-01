import json
import random # to import the random generator function
import time

# TASKS FOR TODAY 31/1/25
# 1 - Learn how to generate random numbers and display them aligned in the output. - COMPLETED
# 2 - Put random number generator in function - COMPLETED
# 3 - create function / logic to assess the sum of the 2 numbers and display correct / incorrect, count correct entries - COMPLETED
# TASKS FOR TODAY 1/2/25
# 4 - add time limit to function before game to run for, say 30s
# 5 - Add high score functionality with .json file
# 6 - Functionality for choosing what to practice
# 7 - Time Trial or number of correct answers function


def random_number_time_trial():
    start_time = time.time()
    correct_answers = 0
    wrong_answers = 0

    elapsed_seconds = 0 # To prevent duplicate prints

    while int(time.time() - start_time) < 10:
        current_second = int(time.time() - start_time)

        if current_second > elapsed_seconds: # Print only when a new second starts
            num = round((random.random()) * 11, )
            num2 = round((random.random()) * 11, )

            print(' ', num, '\n+', num2)  # This prints the 2 random numbers and aligns them in the output, using the add operator - REF TODO #1
            # Ask user for input
            user_input = float(input())  # Otherwise a string was being generated for the input value
            if user_input == num + num2:
                correct_answers += 1
            else:
                wrong_answers += 1
            elapsed_seconds = current_second

            print('correct answers:', correct_answers)
            print('wrong answers:', wrong_answers)
            #TODO these statements are printing in the wrong spot, i want them to print at the end.

    return()

random_number_time_trial()




#
#
# # This function generates 2 random numbers, and displays them on the screen
# ######### THIS CODE WORKS 31/1/25 #########
# def random_number():
#     correct_answers = 0
#     wrong_answers = 0
#     while correct_answers <= 5 and wrong_answers <= 5: # what is with the AND, and how does it work? TODO
#         num = round((random.random()) * 11, )
#         num2 = round((random.random()) * 11, )
#
#         print(' ',num, '\n+',num2) # This prints the 2 random numbers and aligns them in the output, using the add operator - REF TODO #1
#         # Ask user for input
#         user_input = float(input())  # Otherwise a string was being generated for the input value
#         if user_input == num + num2:
#             print("Well Done")
#             correct_answers += 1
#         else:
#             wrong_answers += 1
#         print('correct answers:', correct_answers)
#         print('wrong answers:', wrong_answers)
#     return()
#
# # Call random_number function
# random_number()

#### TODO: #####
# TO DO #1
# include other operators that just add
# I am not fully sure on the string profile here and how / why it is working


######## THIS CODE WORKS ####### 31/1/25
# This code reads in json files from the directory to keep track of high scores
# The 2 functions load the json files and update the json files

# file_path = r"C:\Python Projects\beginning_python\Files\highscore.json"
# # Set the file path as a separate variable so it is easier to change or update in the future. Note no w or r has been assigned
#
#
# def load_high_scores (file_path): # Note - have to include the variables to pass into the function
#     # this finction loads the high scores from the high_scores.json file
#     with open(file_path, 'r') as highscore_file: # read file
#         return json.load(highscore_file)


# def save_high_scores (file_path, data):
#     # thisfunction writes the high scores to the high_scores.json file
#     with open(file_path, 'w') as highscore_file: # write file
#         json.dump(data, highscore_file, indent=4) # Add indent=4 for readability
#     print(f"Data successfully saved to {file_path}")
#
# # High score data to save
# high_scores = [
#     {"player": "Alice", "score": 1000000},
#     {"player": "Bob", "score": 800000},
#     {"player": "Jane", "score": 800}
# ]
#
# # save the data:
# save_high_scores(file_path, high_scores)
#
# #Load the data:
# loaded_data = load_high_scores(file_path)
#
# print("\nData loaded from file:")
# print(loaded_data)

# # This is the initial list for the players and high scores.
#
# # This section of code writes the high scores to a .json file
# with open(r"C:\Python Projects\beginning_python\Files\highscore.json", 'w') as highscore_file:
#     json.dump(high_scores, highscore_file)
#
# print(f"Data successfully written to {highscore_file}")





# f = open("C:/Python Projects/beginning_python/Files/database_file.txt", "r")
# print(f.read())
#
# f.close()

# with open(r"C:\Python Projects\beginning_python\Files\database_file.txt", "a") as f:  #use leading r to get raw read on string
#     f.write("\nhello world")
#     #content = f.read()
#     print(f)

## INTERESTING CODE SNIPPETS AND LEARNINGS##
# 31/1/25
# num = round((random.random())*11,) # I can combine this into one function with the round function, and the random number within this and the multiplier. The purpose of the multiplier is to make the random number bigger than a float between 0 and 1



########################
## This is the time code that prints the number of seconds / runs the loop for a pre-determined number of seconds
# start_time = time.time()
#
# last_printed_second = 0 # To prevent duplicate prints
# print(last_printed_second)
#
# while int(time.time() - start_time) < 10:
#     current_second = int(time.time() - start_time)
#
#     if current_second > last_printed_second: # Print only when a new second starts
#         print(current_second)
#         last_printed_second = current_second
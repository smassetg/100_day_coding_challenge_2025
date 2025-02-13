# This file runs a math game where the user is prompted to choose which mode they want to play and they run a time trial with the program keeping track of the high scores
# Refer progress_log.txt for code comments and indights
# Refer README.md

import json
import random # to import the random generator function
import time
import tkinter as tk

###### Fixed variables
max_number = 11
num, num2 = 0, 0
correct_answers = 0
wrong_answers = 0

###### Program Functions

def countdown(seconds):
    if seconds == -1:
        #root.destroy()
        label6.config(text="Game Over") # Return Game Over message
    else:
        label.config(text=str(seconds))  # Update label text
        root.after(1000, countdown, seconds - 1)  # Call this function again after 1 second

def get_user_input(event=None): # Accept event arguement (required for .bind)
    # Set values to count correct / incorrect answers, set as global variables
    global correct_answers, wrong_answers

    user_answer = entry_box.get().strip()
    print(user_answer)
    entry_box.delete(0, tk.END)

    if user_answer.isdigit() and int(user_answer) == num + num2:
        print("correct")
        correct_answers += 1
    else:
        print("incorrect")
        wrong_answers += 1

    print("Wrong answers:", wrong_answers)
    print("correct answers:", correct_answers)

    generate_numbers() # Calls random number generator within get_user_input

    return(correct_answers, wrong_answers)

def  generate_numbers():
    global num, num2 # store globally so we can access them in get_user_input()
    num, num2 = random.randint(0, max_number), random.randint(0, max_number)
    label2.config(text=str(num))  # Update UI
    label4.config(text=str(num2))  # Update UI


# Initiate the tk windonw
root = tk.Tk()  # Create the main window
math_frame = tk.Frame(root)
math_frame.place(relx=0.5, rely=0.5, anchor="center")  # Centering the frame

root.title("Math Game")  # Set window title
root.geometry("500x500")  # Set window size

# Root label placements
# Label placement, countdown timer, top left
label = tk.Label(root, text="5", font=("Arial", 32))  # Create a label for the countdown
label.place(relx = 1.0, rely = 0.0, x=-25, y = 20, anchor = 'ne')
# Label for user input, alignment under equation
entry_box = tk.Entry(root, font=("Arial", 25), width = 5, justify='center')  # Create an entry_box for the user input
entry_box.place(relx = 0.5, rely = 0.5, x=50, y = 75, anchor = 'ne') # Label placement
entry_box.focus_set() # This makes the cursor active in the box on start up
entry_box.bind("<Return>", get_user_input)
# Label6 placement, "Game Over" message, under entry_box
label6 = tk.Label(root, text="", font=("Arial", 25))  # Create a label for the user input
label6.place(relx = 0.5, rely = 0.5, x=90, y = 150, anchor = 'ne') # Label placement


# Labels for equation figures, grid placement
label2 = tk.Label(math_frame, text = " ", font=("Arial", 32))  # Label for the equation
label2.grid(row=0, column=1, sticky="e")  # Top number
label3 = tk.Label(math_frame, text="+", font=("Arial", 32))  # Label for the equation
label3.grid(row=1, column=0, sticky="e")  # "+" sign
label4 = tk.Label(math_frame, text=" ", font=("Arial", 32))  # Label for the equation
label4.grid(row=1, column=1, sticky="e")  # Bottom number

# Generate random numbers from the start of the root window
generate_numbers()
# call countdown function with # seconds
countdown(4)
# Call mainloop function
root.mainloop()  # Run the Tkinter event loop

print("Wrong answers XXX:", wrong_answers)
print("correct answers XXX:", correct_answers)


# def countdown():
#     start_time = time.time()
#     elapsed_time = 0
#
#     while int(time.time() - start_time) < 5:
#         current_second = int(time.time() - start_time)
#         if current_second > elapsed_time:
#             print(current_second)
#             elapsed_time = current_second



#
# def random_number_time_trial():
#     start_time = time.time()
#     correct_answers = 0
#     wrong_answers = 0
#
#     elapsed_seconds = 0 # To prevent duplicate prints
#
#     while int(time.time() - start_time) < 10:
#         current_second = int(time.time() - start_time)
#
#         if current_second > elapsed_seconds: # Print only when a new second starts
#
#             num, num2 = generate_numbers() # Store the returned values in variables
#             print(' ', num, '\n+', num2)
#             # Ask user for input
#             user_input = float(input())  # Otherwise a string was being generated for the input value
#             if user_input == num + num2:
#                 correct_answers += 1
#             else:
#                 wrong_answers += 1
#             elapsed_seconds = current_second
#
#     print('correct answers:', correct_answers)
#     print('wrong answers:', wrong_answers) # To make the print statements display at the end of the game, they needed to be included within the While loop
#
#
# random_number_time_trial()




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
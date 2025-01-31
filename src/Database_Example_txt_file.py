import json
import random # to import the random generator function

# TASKS FOR TODAY 31/1/25
# 1 - Learn how to generate random numbers and display them aligned in the output.
# 2 - Put random number generator in function
# 3 - create function / logic to assess the sum of the 2 numbers and display correct / incorrect, count correct entries
# 4 - add time limit to function before game ends

# TASK 1 - RANDOM NUMBER GENERATOR
num = random.random()
num2 = round(num*11,1)
print(num)
print(num2)
print(type(num))
print(type(num2))




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


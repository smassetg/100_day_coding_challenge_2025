import json


high_scores = [
    {"player": "Alice", "score": 1000},
    {"player": "Bob", "score": 800}
]
# This is the initial list for the players and high scores.

# This section of code writes the high scores to a .json file
with open(r"C:\Python Projects\beginning_python\Files\highscore.json", 'w') as highscore_file:
    json.dump(high_scores, highscore_file)

print(f"Data successfully written to {highscore_file}")




# f = open("C:/Python Projects/beginning_python/Files/database_file.txt", "r")
# print(f.read())
#
# f.close()

# with open(r"C:\Python Projects\beginning_python\Files\database_file.txt", "a") as f:  #use leading r to get raw read on string
#     f.write("\nhello world")
#     #content = f.read()
#     print(f)


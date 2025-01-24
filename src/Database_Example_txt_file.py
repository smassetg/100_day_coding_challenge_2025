# f = open("C:/Python Projects/beginning_python/Files/database_file.txt", "r")
# print(f.read())
#
# f.close()

with open(r"C:\Python Projects\beginning_python\Files\database_file.txt", "a") as f:  #use leading r to get raw read on string
    f.write("\nhello world")
    #content = f.read()
    print(f)
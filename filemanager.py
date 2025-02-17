import time
import random
import os
print("path for file:")
path = input().strip
print("name of file:")
name = input().strip
print("contents for file:")
with open(path,name,".txt", "w"):
contents = input()
files.write(str(contents))
files.close()
print("Open file? Y/N")
choice = input().strip.lower
    if choice == "y"
with open("readme.txt", "r") as f:
    if choice == "n":
        print("would you like to delete this file? Y/N")
        choice2 = input().strip.lower
        if choice2 == "y":
            if os.path.exists(name,".txt"):
                os.remove(name,".txt")
                if choice2 == "n":
                    print("The file does not exist or cannot be found. creating file...")
                        with open(path,name,".txt", w)
                            print("file created. deleting file...")
                            os.remove(path,name,".txt")
                if choice == else:
                    print("user has made an error.")
        if choice2 == "n":
            print("have a nice day!")
            if choice == else:
                print("user has made an error.")
else:
    print("user has made an error")
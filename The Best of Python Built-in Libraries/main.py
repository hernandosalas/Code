'''
The Best of Python’s Built-in Libraries
https://levelup.gitconnected.com/the-best-of-pythons-built-in-libraries-e08495396ef
'''

'''
Convenient OS functions
'''
def Convenient_OS_functions():
    import os
    ### Execute a shell command
    os.system("echo 'My name is bob the builder'")
    ### Return the current working directory
    os.getcwd()
    ### List all of the files and sub-directories in a particular folder
    os.listdir("Documents")
    ### Create a single folder
    os.mkdir("Data Science Projects")
    ### Create folders recursively
    ### The below line creates a folder "Documents" with a subfolder 
    ### inside it called "Data Science Projects" with a subfolder inside ### that one called "Project 1"
    os.makedirs("Documents/Data Science Projects/Project 1")
    ### Delete a file 
    os.remove("data.txt")  
    ### Delete a folder
    os.rmdir("Data Science Projects")  
    ### Delete directories recursively.
    os.removedirs("Documents/Data Science Projects/Project 1") 
    ### Rename a file or folder
    os.rename("My Documents", "Your Documents")

'''
Easy work with file paths
'''

def Easy_work_with_file_paths():
    import os
    ### Handling slashes / when creating file paths
    file = "process.py"
    folder = "Documents/project1"
    full_path = os.path.join(folder, file)
    ### Get the directory and file name from a full path
    file = os.path.basename(full_path)
    folder = os.path.dirname(full_path)
    ### Check if a file or folder exists
    os.path.exists(full_path)
    ### Get the extension of a file 
    name, extension = os.path.splitext(file)

'''
Working with time
'''

def Working_with_time():
    import time
    import datetime
    import calendar
    ### Get the current date and time
    datetime.datetime.now()
    ### Get just the current time
    datetime.datetime.now().time()
    ### Freeze the program for a set period of time
    time.sleep(secs=5)
    ### Measure runtime of a python command
    start = time.time()
    end = time.time()
    print(end - start)


'''
Functions on lists
'''

def Functions_on_lists():
    ### Sorting a list form low to high
    list_1 = [7, 26, 34, 2, 12, 98, 56]
    list_2 = sorted(list_1)
    ### Getting the max, min, and sum of a list
    list_sum = sum(list_1) 
    max_val = max(list_1)
    min_val = min(list_1)
    ### Convert a string to a list where each element is a character
    list("bob") # ["b", "o", "b"]
    ### You can quickly reverse a list
    list_1.reverse() # [56, 98, 12, 2, 34, 26, 7]
    ### Are any or all of the items in our list True?
    bool_list = [True, False, True, True]
    any(bool_list) #  True
    all(bool_list) # False
    ### You can loop through a list's values AND indices simultaneously
    for index, value in enumerate(list_1):
        "do stuff"

'''
Playing smart with strings
'''

def Playing_smart_with_strings():
    ### Check if a string contains a substring
    sentence = "Hi I'm Bob!"
    if "Bob" in sentence:
        print("YES")
    ### Let's take care of those capital letters too, just in case the ### string for "bOb" looks a little bit different ...
    if "bOb".lower() in sentence.lower():
        print("YES")
    ### These two will convert a string to lower and upper case letters
    sentence.lower()
    sentence.upper()
    ### Check the properties of your string
    sentence.isalpha() # Alphabetic characters only (no symbols or nums)
    sentence.isnumeric() # Numbers only
    sentence.islower() # Is it all lower case?
    sentence.isupper() # Is it all upper case?
    ### Clean up your string
    sentence.capitalize() # First char is capitalized
    sentence.lstrip() # Remove whitespace on left side
    sentence.rstrip() # Remove whitespace on right side
    sentence.strip() # Remove whitespace on both sides
    ### The .join() method can concatenate strings with a separator
    ### list --> string
    " ".join(["Bob","has","a","balloon"])#   "Bob has a balloon"### The .split() method does the opposite of .join()
    ### string --> list
    "Bob has a balloon".split(" ") # ["Bob","has","a","balloon"]
    ### The .replace() method can replace a substring with another
    "Bob has a balloon".replace("has", "is") #"Bob is a balloon"


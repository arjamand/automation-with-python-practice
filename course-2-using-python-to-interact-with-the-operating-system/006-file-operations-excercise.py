# 2024-06-26 11:51:58

''' 
001

1.
Question 1
The create_python_script function creates a new python script in the current working directory, 
adds the line of comments to it declared  by the 'comments' variable, and returns the size of the new file. 
Fill in the gaps to create a script called "program.py".
'''
# import os 

# def create_python_script(filename):
#   comments = "# Start of a new Python program"
#   with open(filename, "w") as file:
#     file.write(comments)
#   filesize = os.path.getsize(filename)
#   return(filesize)

# print(create_python_script("program.py"))

# # out -----> 31





'''
002

Question 
The new_directory function creates a new directory inside the current working directory, 
then creates a new empty file inside the new directory, and returns the list of files in 
that directory. Fill in the gaps to create a file "script.py" in the directory "PythonPrograms". 
'''
# import os

# def new_directory(directory, filename):
#   # Before creating a new directory, check to see if it already exists
#   if os.path.isdir(directory) == False:
#     os.mkdir(directory)

#   # Create the new file inside of the new directory
#   os.chdir(directory)
#   with open (filename,"a") as file:
#     pass

#   # Return the list of files in the new directory
#   return os.listdir()

# print(new_directory("PythonPrograms", "script.py"))

# # out -----> ['script.py']






'''
003

Question 
The file_date function creates a new file in the current working directory, 
checks the date that the file was modified, and returns just the date portion 
of the timestamp in the format of yyyy-mm-dd. Fill in the gaps to create a file 
called "newfile.txt" and check the date that it was modified.
'''
# import os
# import datetime
# from datetime import datetime 

# def file_date(filename):
#   # Create the file in the current directory
#   with open(filename, "a") as test_file:
#     pass
#   timestamp = os.path.getmtime(filename)
#   # Convert the timestamp into a readable format, then into a string
#   date_object = datetime.fromtimestamp(timestamp,)
#   # Return just the date portion 
#   # Hint: how many characters are in “yyyy-mm-dd”? 
#   return ("{}-{}-{}".format(date_object.year, date_object.month, date_object.day))

# print(file_date("newfile.txt")) 
# # Should be today's date in the format of yyyy-mm-dd

# out -----> 2024-6-26

# 2024-06-27 14:35:01

'''
Question 2
Using the CSV file of flowers again, fill in the gaps of the contents_of_file
function to process the data without turning it into a dictionary. How do you skip 
over the header record with the field names?
'''

import os
import csv


# since we already have the file in the dir from prev Q, we'll skipp this funct 
# Create a file with data in it 
# def create_file(filename):
#   with open(filename, "w") as file:
#     file.write("name,color,type\n")
#     file.write("carnation,pink,annual\n")
#     file.write("daffodil,yellow,perennial\n")
#     file.write("iris,blue,perennial\n")
#     file.write("poinsettia,red,perennial\n")
#     file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
  return_string = ""

  # Call the function to create the file 
#   create_file(filename)

  # Open the file
  with open("flowers.csv", "r") as data_file_obj :
    # Read the rows of the file
    rows = csv.reader(data_file_obj)
    # Process each row
    line_count = 0
    for row in rows:
        if line_count != 0:
            name , color, flower_type = row
            # Format the return string for data rows only
            return_string += "a {} {} is {}\n".format(color, name, flower_type)

        line_count += 1


    return return_string

#Call the function
print(contents_of_file("flowers.csv"))


'''
out ---->   a pink carnation is annual
            a yellow daffodil is perennial
            a blue iris is perennial
            a red poinsettia is perennial
            a yellow sunflower is annual
'''
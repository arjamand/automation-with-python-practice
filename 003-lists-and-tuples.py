# 2024-06-18 23:41:01

# #001
# fruits = ["Pineapple", "Banana", "Apple", "Melon"]
# fruits.insert(0, "Orange")
# fruits.insert(25, "Peach")
# print(fruits.index("Peach"))




# #002
# def convert_seconds(seconds):
#   hours = seconds // 3600
#   minutes = (seconds - hours * 3600) // 60
#   remaining_seconds = seconds - hours * 3600 - minutes * 60
#   return (hours, minutes, remaining_seconds)
# result = convert_seconds(5000)
# print(type(result)) # out - <class 'tuple'>


# #003
# # list comprehensions 
# # new_list = [do_something(thing) for thing in list_of_things condition]

# z = [x for x in range(0,101) if x % 3 == 0]
# print(z)


# #004
# # This block of code changes the year on a list of dates.
# # The "years" list is given with existing elements. 
# years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# # The variable "updated_years" is initialized as a list data type 
# # using empty square brackets []. This list will hold the new list
# # with the updated years. 
# updated_years = []
# # The for loop checks each "year" element in the list "years".
# for year in years:
#     # The if-statement checks if the "year" element ends with the 
#     # substring "2023". 
#     if year.endswith("2023"):
#         # If True, then a temporary variable "new" will hold the 
#         # modified "year" element where the "2023" substring is 
#         # replaced with the substring "2024".
#         new = year.replace("2023","2024")
#         # Then, the list "updated_years" is appended with the changed
#         # element held in the temporary variable "new".
#         updated_years.append(new)
#     # If False, the original "year" element will be appended to the 
#     # the "updated_years" list unchanged.
#     else:
#         updated_years.append(year)

# print(updated_years) 
# # Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]



# #005
# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# # Generate new_filenames as a list containing the new filenames
# # using as many lines of code as your chosen method requires.


# new_filenames = []
# for filename in filenames:
#     if filename.endswith("hpp"):
#         new_filenames.append((filename[0:filename.index(".")+1])+"h")
#     else:
#         new_filenames.append(filename)


# print(new_filenames)
# # Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]



#006
filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
new_filenames = [filename.replace(".hpp",".h") if filename.endswith(".hpp") else filename for filename in filenames ]


print(new_filenames) 
# Should print ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
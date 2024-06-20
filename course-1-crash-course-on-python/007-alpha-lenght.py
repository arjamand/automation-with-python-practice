# 2024-06-19 15:18:27

# Complete the for loop and string method needed in this function so that a function call like "alpha_length("This has 1 number in it")" will return the output "17". This function should:

# accept a string through the parameters of the function;

# iterate over the characters in the string;

# determine if each character is a letter (counting only alphabetic characters; numbers, punctuation, and spaces should be ignored);

# increment the counter;

# return the count of letters in the string.

def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for letter in string: 
        # Complete the if-statement using a string method. 
        if letter.isalpha() :
            count_alpha += 1  
    return count_alpha
 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21
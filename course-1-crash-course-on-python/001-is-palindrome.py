def is_palindrome(input_string):
    # Two variables are initialized as string date types using empty 
    # quotes: "reverse_string" to hold the "input_string" in reverse
    # order and "new_string" to hold the "input_string" minus the 
    # spaces between words, if any are found.
    new_string = (input_string.lower()).replace(" ", "")
    reverse_string = new_string[::-1]

    # print(new_string)
    # print(reverse_string)
    # # Complete the for loop to iterate through each letter of the
    # # "input_string"
    # for letter in new_string:

    #     # The if-statement checks if the "letter" is not a space.
    #     if letter != " ":

    #         # If True, add the "letter" to the end of "new_string" and
    #         # to the front of "reverse_string". If False (if a space
    #         # is detected), no action is needed. Exit the if-block.
    #         new_string = ___
    #         reverse_string = ___

    # Complete the if-statement to compare the "new_string" to the
    # "reverse_string". Remember that Python is case-sensitive when
    # creating the string comparison code. 
    if new_string == reverse_string:
        # If True, the "input_string" contains a palindrome.
        return True
    else:
        return False
        
    # Otherwise, return False.
        


print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True
def replace_ending(sentence, old, new):
    # Check if the old substring is at the end of the sentence 
    # print(sentence[(0-(len(old))):],"--------", new)
    # print(sentence[(0-(len(old))):],"-----",new,"-----",sentence[(0-(len(old))):] == old)

    if sentence[(0-(len(old))):] == old:
    # if old in sentence and sentence[sentence.index(old):] == new :
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the 
        # end with the new string
        i = 0-(len(old))
        new_sentence = sentence[:i]+new
        # print(new_sentence)
        return new_sentence


    # Return the original sentence if there is no match 
    return sentence
    
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"

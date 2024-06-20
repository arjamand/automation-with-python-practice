# 2024-06-19 11:26:51

#001 
#iterataing through a dict
# file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
# # for ext, amount in file_counts.items():
# #   print("There are {} files with the .{} extension".format(amount, ext))

# # print("File Count Keys :" , file_counts.keys())
# # print("File Count Values :" , file_counts.values())

# for key, value in file_counts.items():
#     print(key,"\t",value)



# #002
# #The email_list function receives a dictionary, which contains domain names as keys, 
# #and a list of users as values. Fill in the blanks to generate a list that contains 
# #complete email addresses (e.g. diana.prince@gmail.com).

# def email_list(domains):
# 	emails = []
# 	for domain, users in domains.items():
# 	  for user in users:
# 	    emails.append(user+"@"+domain)
# 	return(emails)

# print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))



# 003
# Question 2
# The groups_per_user function receives a dictionary, which contains group names with the list 
# of users. Users can belong to multiple groups. Fill in the blanks to return a dictionary with 
# the users as keys and a list of their groups as values

def groups_per_user(group_dictionary):
    user_groups = {}
	# Go through group_dictionary
    for group, users in group_dictionary.items():
        for user in users:
            if user in user_groups:
                user_groups[user].append(group)
            else:
                user_groups[user] = [group]

		# Now go through the users in the group
        # for user in users:
        #     user_groups[user] = group
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary

    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))
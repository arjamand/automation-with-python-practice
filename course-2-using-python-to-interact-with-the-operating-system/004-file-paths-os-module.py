# 2024-06-25 13:54:41

# Create a directory and move a file from one directory to another
# using low-level OS functions.

import os

# Check to see if a directory named "test1" exists under the current
# directory. If not, create it:


dest_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir) 
#  if not os.path.isfile(os.path.join("test1","READMEEEE.md")):
#     with open(os.path.join("test1","READMEEEE.md")) as file :
#         pass

# Construct source and destination paths:
src_file = os.path.join( "sample_data", "README.md")
dest_file = os.path.join( "test1", "README.md")


# Move the file from its original location to the destination:
os.rename(src_file, dest_file)
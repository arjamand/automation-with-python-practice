# 2024-06-24 13:50:29

with open("poem.txt") as file_opened:
    # print (file_opened.read(),"\n",file_opened.read().count("n")
    print (file_opened)
    lines_in_file = [line.replace("\n","") for line in file_opened if line != "\n"]
    for line in lines_in_file:
        print(line.upper())

    print("Total Number of lines :  ", len(file_opened.readlines()))
        
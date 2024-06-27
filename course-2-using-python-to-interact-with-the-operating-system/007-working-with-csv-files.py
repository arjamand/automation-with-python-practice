# 2024-06-27 13:36:41

import csv 

data_list = [["Name", "Department", "Salary"],
["Aisha Khan", "Engineering", 80000],
["Jules Lee", "Marketing", 67000],
["Queenie Corbit", "Human Resources", 90000]]

with open("data.csv", 'r') as data_file :

    dict_raeder = csv.DictReader(data_file)

    for item in dict_raeder:
        if item["Name"]=="Aisha Khan":
            print(f"Salary of {item["Name"]} is",item["Salary"])

    # csv_file_writer = csv.writer(data_file)
    # csv_file_writer.writerows(data_list)
    # for row in data_list :
    #     csv_file_writer.writerow(row)
    # csv_file_reader = csv.reader(data_file)


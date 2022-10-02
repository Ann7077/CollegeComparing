import university
import university_folder_generator
import csv

# call on university_folder_generator.py

# put everything in college_list.csv as a list
with open('college_list.csv') as f:
    reader = csv.reader(f)
    college_list = list(reader)

# print(college_list) 
# [['ID', 'Name', 'States'], ['209825', 'University of Portland', 'OR'], ['177834', 'A T Still University of Health Sciences', 'OK']]

# print(len(college_list)) 
# 3


# loop through the list (condition: if there are more schools)
    # call on university.py

if __name__ == '__main__':
    row = 1
    while row < len(college_list)+1:
        college = university.university(college_list[row][1], college_list[row][2], college_list[row][0], university_folder_generator.year)
        college.save()
        row = row + 1
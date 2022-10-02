# Generate the folders for all 50 states each named with the state name’s abbreviation

import os
import csv

year = '2022'   # Change manually 

try:
    with open("college_list.csv") as csvfile:
        data = list(csv.DictReader(csvfile))
        states = set(row['States'] for row in data)

        for state in states:
            os.mkdir(rf'../database/{state}')      # State names generated

        for row in data:
            names = row['Names']
            names = names.replace('/','^')
            names = names.replace('?','^')
            names = names.replace(' ','_')         # Replace unecessary things in school name
            os.makedirs(os.path.join(f"..//database//{row['States']}//{names + '_' + str(row['IDs'])}", year))

except FileExistsError:
    pass




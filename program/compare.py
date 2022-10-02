# Read which schools does the user want to compare, find the files for comparing, and merge the csv files

# https://blog.aspose.com/2022/06/09/convert-csv-to-txt-in-python/

import csv
import pandas as pd
import os

with open('compare.csv') as f:
    reader = csv.reader(f)
    compare = list(reader)


try:
    # Find first school csv file in file explore
    file1 = "..//database//" + compare[0][1] + "//" + compare[1][1] + "//" + compare[4][1] + "//" + compare[5][1]
    df1 = pd.read_csv(file1 + ".csv")
    total_cols_1=len(df1.axes[1])
    num1 = total_cols_1 - 2
    df1.head()

    # Copy info into school1.txt
    os.rename(file1 + ".csv", file1 + ".txt")
    with open("school1.txt","a") as f:
        f.write(","+compare[1][1]+num1*','+"\n")
    new_file1 = open("school1.txt", "a")
    with open(file1 + ".txt", "r") as f:
        new_file1.write(f.read())
    new_file1.close()
    os.rename(file1 + ".txt", file1 + ".csv")
    os.rename("school1.txt", "school1.csv")
    df1a = pd.read_csv('school1.csv')
    df1a.head()

    # Find second school csv file in file explore
    file2 = "..//database//" + compare[2][1] + "//" + compare[3][1] + "//" + compare[4][1] + "//" + compare[5][1]
    df2 = pd.read_csv(file2 + ".csv")
    total_cols_2=len(df2.axes[1])
    num2 = total_cols_2 - 2
    df2.head()

    # Copy info into school2.txt
    os.rename(file2 + ".csv", file2 + ".txt")
    with open("school2.txt","a") as f:
        f.write(","+compare[3][1]+num2*','+"\n")
    new_file2 = open("school2.txt", "a")
    with open(file2 + ".txt", "r") as f:
        new_file2.write(f.read())
    new_file2.close()
    os.rename(file2 + ".txt", file2 + ".csv")
    os.rename("school2.txt", "school2.csv")
    df2a = pd.read_csv('school2.csv')
    df2a.head()

except FileNotFoundError:
    print('This file does not exist for one of the schools.')


try:
    # Merge the 2 csv files
    df3 = pd.concat([df1a, df2a.iloc[:,1:]], axis=1)
    # Merged file title
    name = compare[1][1]+'_&_'+compare[3][1]+'_'+compare[5][1]+'_merge.csv'
    df3.to_csv(name, index=False)
    # Delete schoo1.csv and school2.csv
    location = os.getcwd()
    file1 = 'school1.csv'
    path1 = os.path.join(location, file1)
    os.remove(path1)
    file2 = 'school2.csv'
    path2 = os.path.join(location, file2)
    os.remove(path2)
except NameError:
    pass
except PermissionError:
    print('This file already exists')




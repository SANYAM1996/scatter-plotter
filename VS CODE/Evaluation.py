# Write functions for the following tasks

# 1. function to read and print head of train.csv

# 2. function to read and print column names from train.csv

# 3. function to read and print data shape from train.csv


from os.path import dirname, join
current_dir = dirname('train.csv')
file_path = join(current_dir,"train.csv")

import csv
with open('train.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    for line in csv_reader:
        print(line)
# it is showing unicode error and working directory problem while running in vs code but perfectly running in jupyter notebook.
# 0 is the index of column name of train.csv
path = 'train.csv'
lines = [line for line in open(path)]
print(lines[0])
print(lines[1])


 


from sys import argv
from os import listdir, rename
from os.path import isfile
#does some check for valid input

if len(argv) != 2:
    raise Exception("Invalid argument quantity")
files = [f for f in listdir() if isfile(f)]
if not(files):
    raise Exception("No files in directory")

#renames all the files in the passed path
digits_quantity = len(str(len(files) + 1))
for i in range(len(files)):
    dot_index = [j for j in range(len(files[i])) if files[i][j] == '.'][0]
    new_name = argv[1] + str(i+1).zfill(digits_quantity) + files[i][dot_index:]
    rename(files[i], new_name)
print("Success!")
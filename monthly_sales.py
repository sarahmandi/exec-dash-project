# monthly_sales.py

# TODO: import some modules and/or packages here
import csv
import os
import itertools
from operator import itemgetter


##Option C: display list of files to user
path = "/Users/sarahmandi1/Desktop/exec-dash-project/data"
dirs = os.listdir(path)
for file in dirs:
    if file == ".DS_Store":
        pass
    else:
        print(file)
    
#Prompt user to input their selection
while True:
   user_input = input("Please select a file: ")
   break



# monthly_sales.py

# TODO: import some modules and/or packages here
import csv
import os
import itertools
from operator import itemgetter
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import re
import calendar
from matplotlib.ticker import StrMethodFormatter
import pandas as pd

def to_usd(my_price):
  return f"${my_price:,.2f}"

##Option C: display list of files to user
path = os.path.join("data")
dirs = os.listdir(path)

files = []

for file in dirs:
    if file == ".DS_Store":
        pass
    else:
        print(file)
        files.append(file)
    
#Prompt user to input their selection
user_input_file =[]

#print(files)
while True:
    
    user_input = input("Please input a file name: ")
    if user_input in files:
        user_input_file.append(user_input)
        break 
    else:
        print("Sorry, that didn't work. Double check the file name!")
        continue

year_name =[]
month_name =[]

for f in user_input_file:
    year_name.append(int(f[6:-6]))
    month_name.append(int(f[10:-4]))

month = calendar.month_name[month_name[0]] 
year = year_name[0] 

##following is adapted from https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/csv_solution_further.py
CSV_FILENAME = user_input
csv_filepath = os.path.join("data", CSV_FILENAME)
sales = pd.read_csv(csv_filepath)

total_sales = sales["sales price"].sum()

products=sales['product'].unique()
products.sort()
sales_price=sales.groupby(sales['product']).sum()
sales_price_col=list(sales_price['sales price'])
total_price_by_prod=pd.DataFrame({'products':products,'sales_price':sales_price_col})
total_price_by_prod=total_price_by_prod.sort_values(by=['sales_price'],ascending=False)
#print(products)

for i in range(7):
	print(str(i+1)+') '+str(total_price_by_prod.iloc[i][0])+' ' "${0:,.2f}".format(total_price_by_prod.iloc[i][1])
    )

print("-------------------------")
print(f"SALES REPORT!")
print("-------------------------")
print(f"MONTH: {month} {year}")
print(f"TOTAL SALES: {to_usd(total_sales)}")
print("-------------------------")
print("TOP SELLING PRODUCTS:")
print("-----------------------")
print("VISUALIZING THE DATA...")

objects = products
y_pos = np.arange(len(objects))
performance = sales_price_col
 

plt.gca().xaxis.set_major_formatter(StrMethodFormatter('${x:,.0f}'))

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Sales (USD)') 
plt.title('Top-Selling Products (' + month + " " + str(year) +")")
plt.show()
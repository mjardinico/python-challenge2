#load dependencies
import os
import csv

#create path to the CSV file
csv_path = os.path.join(".","Resources","budget_data.csv")

#open the CSV file inside the path
with open(csv_path) as csvfile:

    #initialize the reader
    csvreader = csv.reader(csvfile, delimiter=",") 

    #skip the header
    csvheader = next(csvreader)

    month_count = 0
    total_amount = 0

    for row in csvreader:
        # print(row)  
        month_count += 1
        total_amount += int(row[1])

    print("Financial Analysis")    
    print("----------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total_amount}")
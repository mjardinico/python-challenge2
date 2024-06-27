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
    profit_loss = []

    for row in csvreader:
        # print(row)  
        month_count += 1
        total_amount += int(row[1])
        profit_loss.append(int(row[1]))        
    
    #create a list comprehension for the values to reflect changes profit/loss changes for each month
    changes = [profit_loss[i] - profit_loss[i-1] for i in range(1, len(profit_loss))]
    changes_total = sum(changes)
    average_changes = changes_total / len(changes)

    #find the max() for greateast increase and min() for greatest decrease of values in the list - changes
    greatest_increase = max(changes)
    greatest_decrease = min(changes)

    print("Financial Analysis")    
    print("----------------------------")
    print(f"Total Months: {month_count}")
    print(f"Total: ${total_amount}")  
    print(f"Average Change: ${round(average_changes,2)}")
    print(f"Greatest Increase in Profits: ${greatest_increase}")
    print(f"Greatest Decrease in Profits: ${greatest_decrease}")


        

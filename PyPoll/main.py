# load dependencies
import os
import csv

#create file path
csv_path = os.path.join(".","Resources","election_data.csv")

#initialize the variables dictionary to store the names and votes
vote_dict = {}
total_count = 0

#initialize total_count variable

#open the CSV file
with open(csv_path, 'r') as csvfile:

    #initialize the reader
    csvreader = csv.reader(csvfile, delimiter=",")

    #skip the header
    csvheader = next(csvreader)
    
    # total_count = 0
    # total_votes = 0

    for row in csvreader:
        name = row[2]
        votes = int(row[0])
        total_count += 1
        # total_votes += votes

        if votes in vote_dict:
            vote_dict[name] += votes
        else:
            vote_dict[name] = votes

    
#Determine the winning candidate
winning_candidate = max(vote_dict, key=vote_dict.get)

print("Election Result")
print("--------------------")
print(f"Total Votes: {total_count}")
print("--------------------")
for candidate, val in vote_dict.items():
    # print("--------------------------")
    # print(f"Total Votes: {total_count}")
    # print("--------------------------")
    print(f"{candidate}, {val}")
print("--------------------------")
print(f"Winner: {winning_candidate}")
print("--------------------------")

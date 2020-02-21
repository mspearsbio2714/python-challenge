# Python Challenge | Py Me Up Charlie | PyPoll

# Dependencies 
import os
import csv

# Variables of Interest

total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Set File Path

csv_path = os.path.join("Resources/election_data.csv")
file_output = "Output/poll_results.txt"

# Open & Read CSV
with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csv, delimiter=',')

    # Read the first row of csv file
    csv_header = next(csvreader)

    # Read in each row after the header
    for row in csvreader:

        total_votes +1

        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1

# Calculate % of Votes Won Per Candidate
khan_perc = khan_votes / total_votes
correy_perc = correy_votes / total_votes
li_perc = li_votes / total_votes
otooley_perc = otooley_votes / total_votes

# Calculate Winner based upon Popular Vote

winner = max(knan_votes, correy_votes, li_votes, otooley_votes)

if winner == khan_votes:
    winner_name = "Khan"
elif winner == correy_votes:
    winner_name = "Correy"
elif winner == li_votes:
    winner_name = "Li"
else:
    winner_name = "O'Tooley"

# Print Analysis

print(f"Election Results")
print(f"-------------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------------")
print(f"Khan: {khan_perc:.3%}({khan_votes})")
print(f"Correy: {correy_perc:.3%}({correy_votes})")
print(f"Li: {li_perc:.3%}({li_votes})")
print(f"O'Tooley: {otooley_perc:.3%}({otooley_votes})")
print(f"-------------------------------")
print(f"Winner: {winner_name}")
print(f"-------------------------------")

# Write to text file

output_file = os.path.join('.', 'PyPoll', 'Resources')

with open(file_output, 'w') as file:
    file.write(f"Election Results")
    file.write(f"---------------------")
    file.write(f"Total Votes: {total_votes}")
    file.write(f"---------------------")
    file.write(f"Kahn: {kahn_perc:.3%}({kahn_votes})")
    file.write(f"Correy: {correy_perc:.3%}({correy_votes})")
    file.write(f"Li: {li_perc:.3%}({li_votes})")
    file.write(f"O' Tooley: {otooley_perc:.3%}{otooley_votes}")
    file.write(f"---------------------")
    file.write(f"Winner: {winner_name}")
    file.write(f"---------------------")
# Python Challenge | Py Me Up Charlie | PyBank

# Dependencies 
import os
import csv

# Variables of Interest

tot_months = 0
net_revenue = 0
monthly_change = []
monthly_count = []
greatest_inc = 0
greatest_inc_month = 0
greatest_dec = 0
greatest_dec_month = 0

# File Path and Output File
csv_path = os.path.join("/Users/whodat_saints/Desktop/python-challenge/PyBank/budget_data.csv")
file_output = "raw_data/results.txt"

# Open & Read CSV
with open(csv_path, newline='') as csvfile:

    csvreader = csv.reader(csv, delimiter=',')

    # Read the first row of csv file
    csv_header = next(csvreader)
    row = next(csvreader)

    # Calculate Total Number of Months, Net Amount of "Profit/Losses", Set Variables for Rows

    initial_profit = int(row[1])
    total_months = tot_months +1
    net_revenue = net_revenue + int(row[1])
    greatest_inc = int(row[1])
    greatest_inc_month = row[0]

    # Iterate through rows to calculate 
    for row in csvreader:

        tot_months = total_months +1
        net_revenue = net_revenue + int(row[1])

        # Calculate change from current month to initial months

        change = int(row[1] - initial_profit)
        changes.append(change)
        initial_profit = int(row[1])
        date_count.append(row[0])

        # Calculate the greatest increase
        if int(row[1]) > greatest_inc:
            greatest_inc = int(row[1])
            greatest_inc_month = row[0]

    # Calculating the average
    average_change = sum(changes)/len(changes)

    high = max(changes)
    low = min(changes)

    # Printing all values
    print(f"Financial Analysis")
    print("------------------------")
    print(f"Total Months: {tot_months}")
    print(f"Total: ${net_revenue}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits:, {greatest_inc_month}, max(changes)")
    print(f"Greatest Decrease in Profits:, {greatest_dec_month}, min(changes)")

# Write to text file

with open(file_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------\n")
    file.write("Total Months: %d\n" % tot_months)
    file.write("Total Revenue: $%d\n" % net_revenue)
    file.write("Average Revenue Change $%d\n" % average_change )
    file.write("Greatest Increase in Revenue: %s ($%s)\n" % (biggest_incr[0], biggest_incr[1])"))
    file.write("Greatest Decrease in Revenue: %s ($%s)\n" % (biggest_decr[0], biggest_decr[1])"))



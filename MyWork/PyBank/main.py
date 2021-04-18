# Using budget_data file
# Has Date and Profit/Losses

# Your task is to create a Python script that analyzes the records to calculate each of the following:

    # The total number of months included in the dataset

    # The net total amount of "Profit/Losses" over the entire period

    # Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

    # The greatest increase in profits (date and amount) over the entire period

    # The greatest decrease in losses (date and amount) over the entire period

# Step #1: import modules 
import csv 
import os
# Step #2: read csv file and set path 
budget_csv = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

month = []
profit_loss = []

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    header = next(csv_reader)

    for row in csv_reader:
        month.append(str(row[0]))
        profit_loss.append(int(row[1]))

#total months in dataset
total_months = len(month)

net_profit_loss = 0

for x in profit_loss:
    net_profit_loss = net_profit_loss + x 

average_monthly_change = []
previous_month_amount = 0

for x in range(len(profit_loss)):
    if x == 0:
        previous_month_amount = profit_loss[x] 
    else: 
        monthly_change = profit_loss[x] - previous_month_amount
        average_monthly_change.append(monthly_change)
        previous_month_amount = profit_loss[x]

# average monthly change list 

length = len(average_monthly_change)
total = sum(average_monthly_change)
average_profit_loss = total / length 


date_greatest_increase = ''
amount_greatest_increase = 0
date_greatest_decrease = ''
amount_greatest_decrease = 0

for x in range(len(average_monthly_change)):
    if average_monthly_change[x] > amount_greatest_increase:
        amount_greatest_increase = average_monthly_change[x]
        date_greatest_increase = month[x+1]
    elif average_monthly_change[x] < amount_greatest_decrease:
        amount_greatest_decrease = average_monthly_change[x]
        date_greatest_decrease = month[x+1]


#Print results in Python
print(f'''
Financial Analysis 
-----------------------------------------
Total Months: {total_months}
-----------------------------------------
Total (Net Total): {net_profit_loss}
Average Change: {average_profit_loss}
Greatest Increase in Profits: {date_greatest_increase} ${amount_greatest_increase}
Greatest Decrease in Profits: {date_greatest_decrease} ${amount_greatest_decrease}
''')

#Export text file with the results
output_path = os.path.join("..", "PyBank", "Analysis", "new.csv")

with open(output_path, 'w') as csvfile:

    writer = csv.writer(csvfile, delimiter=',')

    writer.writerow([f"Financial Analysis"])
    writer.writerow([f"-----------------------"])
    writer.writerow([f"Total Months: {total_months}"])
    writer.writerow([f"Total (Net Total): {net_profit_loss}"])
    writer.writerow([f"Average Change: {average_profit_loss}" ]) 
    writer.writerow([f"Greatest Increase in Profits: {date_greatest_increase} ${amount_greatest_increase} "])
    writer.writerow([f"Greatest Decrease in Profits: {date_greatest_decrease} ${amount_greatest_decrease} "])
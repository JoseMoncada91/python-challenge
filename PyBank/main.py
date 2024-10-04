# Module #3 - PyBank - Jose Moncada

# This will allow to create file paths across operating systems.
import os

# Import Module to read CSV File
import csv

# Path for file
csvpath = os.path.join("PyBank", "Resources", "budget_data.csv")

# Define Variables
months = 0 #To store months
net_total = 0  #To store net total of Profit/Losses
previous_profit_loss = None  # To store the profit/loss of the previous month
changes = []  # List to store changes in profit/loss
greatest_increase = 0  # To store the greatest increase in profits
greatest_increase_date = ""  # To store the date of greatest increase
greatest_decrease = 0  # To store the greatest decrease in profits
greatest_decrease_date = ""  # To store the date of greatest decrease

# Read CSV File
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    # Header Skipper
    next(csvreader)  # Skip the header row.

    # Read each row of data after the header.
    for row in csvreader:
        months += 1  # Count the month for each row.
        current_profit_loss = int(row[1])  # Current month's Profit/Loss
        net_total += current_profit_loss  #Add Profit/Loss value to Net Total.
        
# Calculate changes if not the first month
        if previous_profit_loss is not None:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)  # Append change to the list

# Check for greatest increase
            if change > greatest_increase:
                greatest_increase = change  # Update greatest increase
                greatest_increase_date = row[0]  # Update date of greatest increase

# Check for greatest decrease
            if change < greatest_decrease or greatest_decrease == 0:  # Adjust to handle first comparison
                greatest_decrease = change  # Update greatest decrease
                greatest_decrease_date = row[0]  # Update date of greatest decrease
        
        
        previous_profit_loss = current_profit_loss  # Update previous_profit_loss

# Calculate the average change
average_change = sum(changes) / len(changes) if changes else 0

print(f'Financial Analysis')
print(f'Total Months: {months}')
print(f'Net Total Profit/Losses: ${net_total}')
print(f'Average Change in Profit/Losses: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})')
print(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})')

# Export results to a text file
output_path = os.path.join("PyBank", "Analysis", "pybank_jose_analysis.txt")
with open(output_path, 'w') as txtfile:
    txtfile.write(f'Total Months: {months}\n')
    txtfile.write(f'Net Total Profit/Losses: ${net_total}\n')
    txtfile.write(f'Average Change in Profit/Losses: ${average_change:.2f}\n')
    txtfile.write(f'Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n')
    txtfile.write(f'Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n')


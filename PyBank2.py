# -*- coding: utf-8 -*-
"""

@author: Taryn
"""
import os
import csv

budget_data = os.path.join("Module 3\budget_data.csv")

# Function to calculate financial analysis
def calculate_financial_analysis(budget_data):
    total_months = 0
    total_profit_loss = 0
    previous_profit_loss = 0
    change_in_profit_loss = 0
    greatest_increase = {"month": "", "amount": 0}
    greatest_decrease = {"month": "", "amount": 0}
    changes = []

    # Read CSV file
    with open(budget_data.csv, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)  # Skip header row

        for row in csvreader:
            date = row[0]
            profit_loss = int(row[1])

            # Calculate total months and total profit/loss
            total_months += 1
            total_profit_loss += profit_loss

            # Calculate change in profit/loss
            if total_months > 1:
                change_in_profit_loss = profit_loss - previous_profit_loss
                changes.append(change_in_profit_loss)

                # Check for greatest increase and decrease
                if change_in_profit_loss > greatest_increase["amount"]:
                    greatest_increase["month"] = date
                    greatest_increase["amount"] = change_in_profit_loss

                if change_in_profit_loss < greatest_decrease["amount"]:
                    greatest_decrease["month"] = date
                    greatest_decrease["amount"] = change_in_profit_loss

            # Update previous profit/loss
            previous_profit_loss = profit_loss

    # Calculate average change
    average_change = sum(changes) / len(changes)

    # Print results
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total_profit_loss}")
    print(f"Average Change: ${average_change:.2f}")
    print(f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['amount']})")
    print(f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['amount']})")
    
    # Write results to text file
    output_file = open("output.txt", "w")
    output_file.write("Financial Analysis\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_profit_loss}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase['month']} (${greatest_increase['amount']})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease['month']} (${greatest_decrease['amount']})\n")
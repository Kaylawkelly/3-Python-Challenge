#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 21:19:59 2021

@author: kay
"""
import csv
import os

csvpath = os.path.join('Resources', 'budget_data.csv')
pathout = os.path.join('Analysis','budget_analysis.txt')

total_months = []
revenue = []
average_revenue_change = []
monthly_change = []


with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    print(reader)
    csvheader = next(reader)
    
    print(f"Header: {csvheader}")               

#Total Months       
    for row in reader:
        total_months.append(row[0])
        revenue.append(row[1])
    print(len(total_months))
    
#Total Revenue 
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)

 #Average Monthly Change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
 

        average_revenue_change.append(profit_loss)
    Total = sum(average_revenue_change)
    monthly_change = Total / len(average_revenue_change)
    print(monthly_change)
   
#Greatest Increase in Profits
    greatest_increase = max(average_revenue_change)
    print(greatest_increase)
    j = average_revenue_change.index(greatest_increase)
    month_increase = total_months[j+1]
    
#Greatest Decrease in Profits
    greatest_decrease = min(average_revenue_change)
    print(greatest_decrease)
    x = average_revenue_change.index(greatest_decrease)
    month_decrease = total_months[x+1]


print(f'Financial Analysis'+'\n')
print(f'------------------------------------'+'\n')
print("Total Months: " + str(len(total_months)))
print("Total: $ " + str(total_revenue))   
print("Average Change: $" + str(monthly_change))
print(f"Greatest Increase in Profits: {month_increase} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})")

file = open(pathout,'w')


file.write(f'Financial Analysis'+'\n')
file.write(f'--------------------------------'+'\n')
file.write("Total Months: " + str(len(total_months)))
file.write("Total: $ " + str(total_revenue)) 
file.write("Average Change: $" + str(monthly_change))
file.write(f"Greatest Increase in Profits: {month_increase} (${greatest_increase})")
file.write(f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})")
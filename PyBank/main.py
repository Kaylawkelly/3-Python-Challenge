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
average_change = []


with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    print(reader)
    csvheader = next(reader)
    print(f"Header: {csvheader}")               

#Total Months as a list       
    for row in reader:
        total_months.append(row[0])
        revenue.append(row[1])
    print(len(total_months))
    
#Total Revenue As List and Conversion to INT
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)

 #Average Change
    i = 0
    for i in range(len(revenue) - 1):
        profit_loss = int(revenue[i+1]) - int(revenue[i])
        average_revenue_change.append(profit_loss)
        
    Total = sum(average_revenue_change)
    average_change = Total / len(average_revenue_change)
    print (round(average_change))
   
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


print('Financial Analysis'+'\n')
print('------------------------------------'+'\n')
print("Total Months: " + str(len(total_months))+'\n')
print("Total: $ " + str(total_revenue)+'\n')   
print("Average Change: $" + str(round(average_change,2))+'\n')
print(f"Greatest Increase in Profits: {month_increase} (${greatest_increase})"+'\n')
print(f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})"+'\n')

file = open(pathout,'w')


file.write('Financial Analysis'+'\n')
file.write('--------------------------------'+'\n')
file.write("Total Months: " + str(len(total_months))+'\n')
file.write("Total: $ " + str(total_revenue)+'\n') 
file.write("Average Change: $" + str(round(average_change,2))+'\n')
file.write(f"Greatest Increase in Profits: {month_increase} (${greatest_increase})"+'\n')
file.write(f"Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})"+'\n')
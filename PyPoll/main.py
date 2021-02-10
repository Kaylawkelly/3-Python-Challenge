#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 21:29:00 2021

@author: kay
"""
import os
import csv

csvpath = os.path.join("Resources","election_data.csv")
pathout = os.path.join("Analysis","election_analysis.txt")


totalVotes = 0
candidates = []
votecount = []
winnervotercount = 0




with open(csvpath, 'r', newline='') as csvfile:        
    
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)


    for row in csvreader:
        totalVotes += 1

        if(row[2] not in candidates):
            candidates.append(row[2])
            votecount.append(0)
        
       
        candidateIndex = candidates.index(row[2])
        votecount[candidateIndex] += 1

#Within

    print('Election Results'+'\n')
    print('------------------------------------'+'\n')
    print(f"Total votes: {totalVotes}")
    print('------------------------------------'+'\n')
    
    for x in range(len(candidates)):
        votePercent = round((votecount[x]/totalVotes)*100,3)
        print(f"{candidates[x]}: {votePercent}% ({votecount[x]})")
        if (winnervotercount<votecount[x]):
            winnervotercount = votecount[x]
            winner = candidates[x]
    
    print('------------------------------------'+'\n')
    print(f"Winner: {winner}")
    print('------------------------------------'+'\n')

file = open(pathout,'w')


file.write("Election Anaylsis\n")
file.write('------------------------------------'+'\n')
file.write("\nTotal votes:" + str(totalVotes))
file.write("\n-------------------------------------------")
    
for x in range(len(candidates)):
    votePercent = round((votecount[x]/totalVotes)*100,3)
    file.write("\n" + str(candidates[x]) +" : " + str(votePercent) 
                + "% ("+ str(votecount[x]) + ")")
file.write("\n-------------------------------------------")
file.write("\nWinner: " + str(winner))
file.write("\n-------------------------------------------")

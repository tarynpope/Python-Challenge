# -*- coding: utf-8 -*-
"""

@author: Taryn
"""

import os
import csv

#Set file path
Pollingcsv = os.path.join("Resources\election_data.csv")

#Define variables 
Tally= 0
vote_count = []
vote_percentage= []
Candidates_list = []
Candidate_indv = []

#Count election results 
with open(Pollingcsv, newline="") as csvfile:
    csvreader= csv.reader(csvfile, delimiter= ",")
    csv_header = next(csvreader)
    for row in csvreader:
        Tally = Tally+1
        Candidates_list.append(row[2])
        #X - candidate names #y- votes per candidate #z- vote percentage
    for x in set(Candidates_list):
        Candidate_indv.append(x)
        y = Candidates_list.count(x)
        vote_count.append(y)
        z= (y/Tally)*100
        vote_percentage.append(z)
        
#Calculate winning candidate 
Winner= max(vote_count)
winning_candidate = Candidate_indv[vote_count.index(Winner)]

print("Election Results")
print("Total Votes:"+ str(vote_count))
print("The winner is: " + winning_candidate)

# Print or write results to a file
with open("election_results.txt", "w") as output_file:
    output_file.write("Election Results\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Total Votes: {Tally}\n")
    output_file.write("----------------------------\n")
    for i in range(len(Candidate_indv)):
        output_file.write(f"{Candidate_indv[i]}: {vote_percentage[i]:.3f}% ({vote_count[i]})\n")
    output_file.write("----------------------------\n")
    output_file.write(f"Winner: {winning_candidate}\n")
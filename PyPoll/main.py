import os 
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

Total_Votes=[]

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    
    for row in csvreader:
        Total_Votes.append(row[2])
        
Total= len(Total_Votes)

Total_C=[]
for Charles in Total_Votes:
    if Charles == "Charles Casper Stockham":
        Total_C.append(Charles)
Total_C_Count = len(Total_C)

Total_D=[]
for Diana in Total_Votes:
    if Diana == "Diana DeGette":
        Total_D.append(Diana)
Total_D_Count = len(Total_D)

Total_R=[]
for Raymon in Total_Votes:
    if Raymon == "Raymon Anthony Doane":
        Total_R.append(Raymon)
Total_R_Count = len(Total_R)

# C_Percentage= round(Total_C_Count/Total)*100 
Winnerlist= [Total_C_Count,Total_D_Count,Total_R_Count]
PotentialWinners= ["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]
Winner = Winnerlist.index(max(Winnerlist))
Results=(
    f"Election Results\n"
    f"-----------------------------------\n"
    f"Total Votes: {Total}\n"
    f"-----------------------------------\n"
    f"Charles Casper Stockham: {round((Total_C_Count/Total)*100,3)}% ({Total_C_Count})\n"
    f"Diana DeGette: {round((Total_D_Count/Total)*100,3)}% ({Total_D_Count})\n"
    f"Raymon Anthony Doane: {round((Total_R_Count/Total)*100,3)}% ({Total_R_Count})\n"
    f"-----------------------------------\n"
    f"Winner: {PotentialWinners[Winner]}\n"
    f"-----------------------------------\n")
print(Results)
Analysis = open("Analysis/analysis_output.txt", "w")
Analysis.write(Results)
Analysis.close()
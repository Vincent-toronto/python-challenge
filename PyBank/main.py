import os 
import csv
# there is no avg in python neeed to import module to have mean
from statistics import mean
csvpath = os.path.join('Resources', 'budget_data.csv')

Month=[]
Total=[]
Change=[]

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first 
    csv_header = next(csvreader)
    
    previous_value = 0
    # # # Read each row of data after the header
    for row in csvreader:
        #current value is first row
        current_value=int(row[1])
        Month.append(row[0])
        Total.append(int(row[1]))
        Monthly_Change= (current_value - previous_value)
        # position matters previous valuse = the current value after the for loop runs
        previous_value=current_value
        Change.append (Monthly_Change)
        Total_months= len(Month)
        # There is no previous data first entry should be 0
        Change[0]= 0
# move out of for loop so the processed data is not manipulated - use indents to leave for loop
#find the index valuse in the list for the max change as month_max then take the index value to find the corresponding Month with the same index
Month_Max= Change.index(max(Change))
Month_Min= Change.index(min(Change))     
#remove first entry in the list
Change.pop(0)
        
Results=(
    f"FINANCIAL ANALYSIS\n"
    f"-----------------------------------\n"
    f"Total Months: {Total_months}\n"
    f"Total: ${sum(Total)}\n"
    f"Change: {round(mean(Change),2)}\n"
# Month index takig month list and finding the index number of month change
    f"Greatest Increase in Profits: {Month[Month_Max]} ({max(Change)})\n"
    f"Greatest Decrease in Profits: {Month[Month_Min]} ({min(Change)})")

print (Results)

# to write to new file you need to open it and write then write your output
Analysis = open("Analysis/analysis_output.txt", "w")
Analysis.write(Results)
Analysis.close()
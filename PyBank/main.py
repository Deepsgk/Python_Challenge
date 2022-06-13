import os
import csv
from statistics import mean
# created this common path for both the projects- bank and poll
# Join various path components
csvpath= os.path.join('Resources', 'budget_data.csv').replace("\\","/")
with open (csvpath,newline='') as csvfile:
   csvreader = csv.reader(csvfile,delimiter=',')
   csv_header = next(csvreader)
   rows_list=list(csvreader)
   months=[]
   Profit_and_loss = []
   total_months=0
   total_Profit_and_loss=0
   monthly_PL_changes=[]
   for row in rows_list:
      months.append(row[0])
      total_months= len(months)
 
      total_Profit_and_loss += int(row[1])
      Profit_and_loss.append(row[1])
 
i=0
for i in range(len(Profit_and_loss)-1):
    profit_change= int(Profit_and_loss[i+1]) - int(Profit_and_loss[i])
    monthly_PL_changes.append(profit_change)
    i += 1
    Average_change= mean(monthly_PL_changes)
 
    Greatest_increase = max(monthly_PL_changes)
    Greatest_decrease = min(monthly_PL_changes)
    x= monthly_PL_changes.index(Greatest_increase)
    y= monthly_PL_changes.index(Greatest_decrease)
    month_highest_increase= months[x+1]
    month_highest_decrease= months[y+1]


print("Financial Analysis")
print("-"*50)
print(f"Total Months: {total_months}")
print(f"Total Profit_and Loss:${total_Profit_and_loss}")    
print(f"Average of changes: ${Average_change:.2f}")   
print(f"Greatest Increase: {month_highest_increase}  (${Greatest_increase})")
print(f"Greatest Decrease: {month_highest_decrease}  (${Greatest_decrease})")

outputfile='Summary_of_Financial_Analysis.txt'

with  open(outputfile, 'w') as output:
   output.write("Financial Analysis\n")
   output.write("-"*50+"\n")
   output.write(f"Total Months: {total_months}\n")
   output.write(f"Total Profit_and Loss:${total_Profit_and_loss}\n")    
   output.write(f"Average of changes: ${Average_change:.2f}\n")   
   output.write(f"Greatest Increase: {month_highest_increase}  (${Greatest_increase})\n")
   output.write(f"Greatest Decrease: {month_highest_decrease}  (${Greatest_decrease})\n")



    




      







 

   









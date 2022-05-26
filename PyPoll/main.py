import os
import csv
from statistics import mean
# created this common path for both the projects- bank and poll
pathlead ='C:/Users/deepa/Desktop/Python_Challenge/' 
# Join various path components
csvpath= os.path.join(pathlead, 'Resources', 'election_data.csv').replace("\\","/")
with open (csvpath,newline='') as csvfile:
   csvreader = csv.reader(csvfile,delimiter=',')
   csv_header = next(csvreader)
   rows_list=list(csvreader)
   votes_cast=[]
   total_votes=0
   County=[]
   Electionlist=[]
   Khan=[]
   Li=[]
   Correy =[]
   OTooley=[]
   
   for row in rows_list:
      votes_cast.append(row[0])
      County.append(row[1])
      Electionlist.append(row[2])
      total_votes= len(votes_cast)

for candidates in Electionlist:
    if  candidates == "Khan":
          Khan.append(candidates)
          khanvotes = len(Khan)

    elif candidates == "Correy":
           Correy.append(candidates)
           correyvotes = len(Correy)

    elif  candidates == "Li":
           Li.append(candidates)
           livotes = len(Li)
    else:  
         candidates == "OTooley"
         OTooley.append(candidates)
         otooleyvotes= len(OTooley)
      
#Each Candidate Percentage of votes on total votes
khan_percent = round(((khanvotes / total_votes) * 100),2)
correy_percent = round(((correyvotes/ total_votes) * 100), 2)
li_percent = round(((livotes/ total_votes) * 100), 2)
otooley_percent = round(((otooleyvotes / total_votes) * 100), 2)

if khan_percent > max(correy_percent, li_percent, otooley_percent):
        winner = "Khan"
elif correy_percent > max(khan_percent, li_percent, otooley_percent):
        winner = "Correy"  
elif li_percent > max(correy_percent, khan_percent, otooley_percent):
        winner = "Li"
else:
     winner = "O'Tooley"

Percentage_list ={"Khan": {khan_percent} ,"Correy":{correy_percent},"Li": {li_percent},"OTooley":{otooley_percent}}
max_value = max(Percentage_list.items(), key=lambda item:item[1])    



print("Election results")
print("-"*100)
print(f"Total Votes: {total_votes}")
print("-"*100)
print(f'Khan: {khan_percent:.3f}% ({khanvotes})' + '\n')
print(f'Correy: {correy_percent:.3f}% ({correyvotes})' + '\n')
print(f'Li: {li_percent:.3f}% ({livotes})' + '\n')
print(f"O'Tooley: {otooley_percent:.3f}% ({otooleyvotes})" + '\n')
print("-"*100)
print(f'Winner: {winner:}' + '\n')
print("-"*100)
print(f'Winner: {max_value}' + '\n')
print("-"*100)


outputfile='Summary_of_Election_Analysis.txt'

with  open(outputfile, 'w') as output:
    output.write("Election results\n")
    output.write("-"*100+"\n")
    output.write(f"Total Votes: {total_votes}\n")
    output.write("-"*100+"\n")
    output.write(f'Khan: {khan_percent:.3f}% ({khanvotes})' + '\n')
    output.write(f'Correy: {correy_percent:.3f}% ({correyvotes})' + '\n')
    output.write(f'Li: {li_percent:.3f}% ({livotes})' + '\n')
    output.write(f"O'Tooley: {otooley_percent:.3f}% ({otooleyvotes})" + '\n')
    output.write("-"*100+"\n")
    output.write(f'Winner: {winner:}' + '\n')
    output.write("-"*100+"\n")
    output.write(f'Winner: {max_value}' + '\n')
    
   







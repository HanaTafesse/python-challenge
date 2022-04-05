import os
import csv

print("Election Results")
print("----------------------------")

election_data = os.path.join('PyPoll\Resources\election_data.csv')

total_votes = 0
candidates = []
num_votes = []

with open(election_data, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    row=next(csvread)

    for row in csvread:
        candidate=row[2]
        total_votes += 1
        if candidate in candidates:
            index=candidates.index(candidate)
            num_votes[index]+= 1
        else:
            candidates.append(candidate)
            num_votes.append(1)
print(f"Total Votes: {total_votes}")
print("----------------------------")

percent = []
maxvote=num_votes[0]
maxindex=0

for count in range(len(candidates)):
    vote_percent=round(num_votes[count]/total_votes*100,3)
    percent.append(vote_percent)
    print (f"{candidates[count]}: {percent[count]}% ({num_votes[count]})")
    if num_votes[count]>maxvote:
        maxvote=num_votes[count]
        maxindex=count    
winner=candidates[maxindex]

print("----------------------------")
print(f"Winner: {winner}")
print("----------------------------")


with open("MyFile.txt",'w') as file1:
  
    file1.write("Election Results \n")
    file1.write("----------------------------\n")
    file1.write(f"Total Votes: {total_votes} \n")
    file1.write("----------------------------\n")
    for count in range(len(candidates)):
     file1.write (f"{candidates[count]}: {percent[count]}% ({num_votes[count]}) \n")
    file1.write("---------------------------- \n")
    file1.write(f"Winner: {winner} \n ")
    file1.write("----------------------------\n")







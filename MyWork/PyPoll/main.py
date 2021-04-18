#import modules
import os 
import csv

#read csv file and set path
election_csv = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

candidate_dictionary = {}

#read in the csv file
with open(election_csv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    for row in csv_reader:
        candidate = row[2]
        if candidate in candidate_dictionary:
            candidate_dictionary[candidate] = candidate_dictionary[candidate] + 1
        else:
            candidate_dictionary[candidate] = 1

total_votes = sum(candidate_dictionary.values())

#total votes by candidates
khan_total_votes = (candidate_dictionary["Khan"])
correy_total_votes = (candidate_dictionary["Correy"])
li_total_votes = (candidate_dictionary["Li"])
otooley_total_votes = (candidate_dictionary["O'Tooley"])

#percentage votes by candidates
khan_percentage_votes = khan_total_votes / (total_votes) * 100
correy_percentage_votes = correy_total_votes / (total_votes) * 100
li_percentage_votes = li_total_votes / (total_votes) * 100
otooley_percentage_votes = otooley_total_votes / (total_votes) * 100

#determine winner by popular votes
winner = ""

if khan_total_votes > correy_total_votes and khan_total_votes > li_total_votes and khan_total_votes > otooley_total_votes:
    winner = "Khan"
elif li_total_votes > correy_total_votes and li_total_votes > khan_total_votes and li_total_votes > otooley_total_votes:
    winner = "Li"
elif correy_total_votes > khan_total_votes and correy_total_votes > li_total_votes and correy_total_votes > otooley_total_votes:
    winner = "Correy"
else:
    winner = "O'Tooley"

#print to Python
print(f'''
Election Results
---------------------------------
Total Votes: {total_votes}
---------------------------------
Khan:    {khan_percentage_votes}% {khan_total_votes}
Correy:  {correy_percentage_votes}% {correy_total_votes}
Li:      {li_percentage_votes}% {li_total_votes}
O'Tooley: {otooley_percentage_votes}% {otooley_total_votes}
---------------------------------
Winner: {winner}
''')

#write to a csv file output
output_path = os.path.join("..", "PyPoll", "Analysis", "new.csv")

with open(output_path, 'w') as csvfile:

    writer = csv.writer(csvfile, delimiter=',')

    writer.writerow([f"Election Results"])
    writer.writerow([f"-----------------------"])
    writer.writerow([f"Total Votes: {total_votes}"])
    writer.writerow([f"-----------------------"])
    writer.writerow([f"Khan: {khan_percentage_votes}% {khan_total_votes}"])
    writer.writerow([f"Correy: {correy_percentage_votes}% {correy_total_votes}"])
    writer.writerow([f"Li: {li_percentage_votes}% {li_total_votes}"])
    writer.writerow([f"O'Tooley: {otooley_percentage_votes}% {otooley_total_votes}"])
    writer.writerow([f"-----------------------"])
    writer.writerow([f"Winner: {winner}"])
    writer.writerow([f"-----------------------"])
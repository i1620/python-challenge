import csv
import os

#empty lists
total_votes = []
candidates = []
candidate_1 = []
candidate_2 = []
candidate_3 = []
candidate_4 = []

electionFilePath = os.path.join("Resources/" + "election_data.csv")

#read csv
with open(electionFilePath ) as csvFile:
    csvReader = csv.reader(csvFile, delimiter=",")

    csvRow = next(csvReader)

#find total number of votes cast
    for row in csvReader:
        total_votes.append(row[0])
        candidates.append(row[2])

    t_votes = len(total_votes)

    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {t_votes}")
    print("-----------------------------")

#find number of votes for each candidate
    for row[2] in candidates:
        if row[2] == "Khan":
            candidate_1.append(candidates)
            c1_votes = len(candidate_1)
        elif row[2] == "Correy":
            candidate_2.append(candidates)
            c2_votes = len(candidate_2) 
        elif row[2] == "Li":
            candidate_3.append(candidates)
            c3_votes = len(candidate_3)
        else:
            candidate_4.append(candidates)
            c4_votes = len(candidate_4)
    
#find percentage of votes for each candidate
    c1_percent = format(round(((c1_votes/t_votes)*100), 2),'.3f')
    c2_percent = format(round(((c2_votes/t_votes)*100), 2),'.3f')
    c3_percent = format(round(((c3_votes/t_votes)*100), 2), '.3f')
    c4_percent = format(round(((c4_votes/t_votes)*100), 2), '.3f')

    print(f"Khan: {c1_percent}% ({c1_votes})")
    print(f"Correy: {c2_percent}% ({c2_votes})")
    print(f"Li: {c3_percent}% ({c3_votes})")
    print(f"O'Toole: {c4_percent}% ({c4_votes})")
    print("-----------------------------")

#find winner
    if c1_percent > max(c2_percent, c3_percent, c4_percent):
        winner = "Khan"
    elif c2_percent > max(c1_percent, c3_percent, c4_percent):
        winner = "Correy"
    elif c3_percent > max(c1_percent, c2_percent, c4_percent):
        winner = "Li"
    else:
        winner = "O'Toole"
    
    print(f"Winner: {winner}")
    print("-----------------------------")

outputPath = os.path.join("analysis/" + "PyPoll.py")
with open(outputPath, 'w+', newline='') as text_file:

    print("Election Results", file=text_file)
    print("-----------------------------", file=text_file)
    print(f"Total Votes: {t_votes}", file=text_file)
    print("-----------------------------", file=text_file)
    print(f"Khan: {c1_percent}% ({c1_votes})", file=text_file)
    print(f"Correy: {c2_percent}% ({c2_votes})", file=text_file)
    print(f"Li: {c3_percent}% ({c3_votes})", file=text_file)
    print(f"O'Toole: {c4_percent}% ({c4_votes})", file=text_file)
    print("-----------------------------", file=text_file)
    print(f"Winner: {winner}", file=text_file)
    print("-----------------------------", file=text_file)

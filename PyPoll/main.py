import csv
import os

election_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'Resources', 'election_data.csv')
with open(election_file, newline='', encoding='utf-8') as f:
    data = list(csv.reader(f))[1:]

candidates = {}
for line in data:
    ballot_id, county, candidate = line[0], line[1], line[2]
    if candidate not in candidates:
        candidates[candidate] = 1
    else:
        candidates[candidate] += 1

total_votes = sum(candidates.values())

output = []
output.append("Election Results")
output.append('-'*25)
output.append("Total Votes: " + str(total_votes))
output.append('-'*25)
for c in sorted(candidates.keys()):
    percentage = str(round(((int(candidates[c]) / total_votes) * 100), 3))
    output.append(f"{c}: {percentage}% ({candidates[c]})")

winner = max(candidates, key=candidates.get)

output.append('-'*25)
output.append(f"Winner: {winner}")

output_file = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'analysis', 'output.txt')
with open(output_file, 'w') as f:
    for x in output:
        print(x, "\n")
        f.write(x + "\n")

import pandas as pd

file_path = 'election_data.csv'
df = pd.read_csv(file_path)

total_votes = df.shape[0]

vote_counts = df['Candidate'].value_counts()

vote_prcnt = (vote_counts / total_votes) * 100

winner = vote_counts.idxmax()
winner_votes = vote_counts.max()

print("Election Results")
print(f"Total Votes: {total_votes}")
for candidate, votes in vote_counts.items():
    percentage = vote_prcnt[candidate]
    print(f"{candidate}: {percentage:.3f}% ({votes})")
print(f"Winner: {winner}")

with open('election_results.txt', 'w') as file:
    file.write("Election Results\n")
    file.write(f"Total Votes: {total_votes}\n")
    for candidate, votes in vote_counts.items():
        percentage = vote_prcnt[candidate]
        file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    file.write(f"Winner: {winner}\n")

print("Analysis has been written to election_results.txt")
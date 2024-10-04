# Module #3 - PyPoll - Jose Moncada

# This will allow to create file paths across operating systems.
import os

# Import Module to read CSV File
import csv

# Path for file
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

# Define Variables
voters = 0  # To store voters
candidates = set()  # To store unique candidates
candidate_votes = {}  # To store votes for each candidate

# Read CSV File
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)

    # Header Skipper
    next(csvreader)  # Skip the header row.

    # Read each row of data after the header.
    for row in csvreader:
        voters += 1  # Count the votes for each row.
        candidate = row[2]  # Get the candidate from column C
        
        # Add the candidate to the set and count the votes
        candidates.add(candidate)  # Add the candidate to the set.
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1  # Increment vote count.
        else:
            candidate_votes[candidate] = 1  # Initialize vote count

# Print total votes after the counting is done
print(f'Election Results')  
print(f'Total votes: {voters}')  

for candidate, votes in candidate_votes.items():
    percentage = (votes / voters) * 100  # Calculate percentage
    print(f"{candidate}: {percentage:.3f}% ({votes})")

# Determine the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)
winner_votes = candidate_votes[winner]

# Print the winner
print(f"\nWinner: {winner} with {winner_votes} votes")

# Export the results to a text file
output_path = os.path.join("PyPoll", "Analysis", "pypoll_jose_analysis.txt")

with open(output_path, 'w') as txtfile:
    txtfile.write('Election Results\n')
    txtfile.write(f'Total votes: {voters}\n\n')
    for candidate, votes in candidate_votes.items():
        percentage = (votes / voters) * 100  # Calculate percentage
        txtfile.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    
    txtfile.write(f"\nWinner: {winner} with {winner_votes} votes\n")
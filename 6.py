#Timofey

total_parties = 5
votes = {i: 0 for i in range(1, total_parties + 1)}
spoiled_ballots = 0

with open("votes.txt", "r") as file:
    results = file.read().split()

for vote in results:
    try:
        vote_num = int(vote)
        if vote_num in votes:
            votes[vote_num] += 1
        else:
            spoiled_ballots += 1
    except ValueError:
        spoiled_ballots += 1

total_votes = sum(votes.values()) + spoiled_ballots

results = []
for party, count in votes.items():
    percentage = (count / total_votes * 100) if total_votes > 0 else 0
    results.append((party, count, percentage))

results.sort(key=lambda x: x[1], reverse=True)

print("Підсумки виборів:")
for i, (party, count, percentage) in enumerate(results, start=1):
    print(f"{i}. Партія №{party} | {count} | {percentage:.2f}%")

spoiled_percentage = (spoiled_ballots / total_votes * 100) if total_votes > 0 else 0
print(f"\nЗіпсовані бланки | {spoiled_ballots} | {spoiled_percentage:.2f}%")
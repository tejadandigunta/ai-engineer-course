scores = []

for i in range(1, 6):
    score = int(input(f"Enter score of player{i}: "))
    scores.append(score)

total_score = sum(scores)
highest_score = max(scores)
print(total_score)
print(highest_score)

count = 0
for score in scores:
    if score >= 50:
        count += 1

print(f"Number of 50+ Scores: {count}")
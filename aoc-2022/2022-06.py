from string import ascii_lowercase

K = 14

with open("day06.txt") as f:
    msg = f.read()

letter_counts = {l: 0 for l in ascii_lowercase}
for i in range(K):
    letter_counts[msg[i]] += 1

i = K
while letter_counts[msg[i]] > 1 or letter_counts[msg[i-K]] > 1 or max(letter_counts.values()) > 1:
    letter_counts[msg[i]] += 1
    letter_counts[msg[i-K]] -= 1
 
    i += 1

print(msg[i-3:i+1])
print(i)
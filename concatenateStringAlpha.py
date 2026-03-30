words = []
n = int(input())
for i in range(n):
    words.append(str(input()))
sorted_words = sorted(words)
print(sorted_words[0] + sorted_words[1])
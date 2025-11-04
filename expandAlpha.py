S = input().strip()

if '_' in S:
    index = S.index('_')
    result = S[:index][::-1] + S[index:]
else:
    result = S[::-1]

print(result)

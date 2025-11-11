time = list(map(str, input().split()))
stored_time = []
for i in time:
    stored_time.append(i.split(':'))
print(stored_time)
count = 0
for j in stored_time:
    first = j[0]
    second = j[1]
    if int(first) > 10 and int(second) >= 0:
        count += 1
    elif int(first) == 10 and int(second) > 0:
        count += 1
    elif int(first) == 10 and int(second) == 0:
        count += 0
print(count)

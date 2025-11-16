s = str(input().strip().lower())


#  simple to print the string in descending order
# print(''.join(sorted(s, reverse=True))) 


# to print the string in descending order without duplicates
s_noduplicates = ''.join(sorted(set(str(input().strip().lower())), reverse=True))
print(s_noduplicates)

# one liner
print(''.join(sorted(set(str(input().strip().lower())), reverse=True)))
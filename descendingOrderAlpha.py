s = str(input().strip().lower())


#  simple to print the string in descending order
# print(''.join(sorted(s, reverse=True))) 


# to print the string in descending order without duplicates
s_noduplicates = ''.join(sorted(set(s), reverse=True))
print(s_noduplicates)
def frequency_count(string, freq, length):
    for i in range(length):
        freq[ord(string[i]) - ord('a')] += 1
    return freq

# using hashmap
def hashmap(string):
    frequency = {}
    for ch in string:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1
    return frequency

string = str(input().strip()).lower() #edge case of what if there's a mix of upper and lower case in the input
length = len(string)
freq = [0] * 26 # total number of alphabets is 26
print("Frequency using array \n", frequency_count(string, freq, length))
print("Frequency using hashmap \n", hashmap(string))


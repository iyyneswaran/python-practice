s = str(input("Enter a string: "))
vowels, consonants, sc, n = 0, 0, 0, 0
vowel ='aeiouAEIOU'
special_characters = '''!@#$%^&*()-+?_=,<>/'''
for char in s:
    if char.isalpha():
        if char in vowel:
            vowels += 1
        else:
            consonants += 1
    elif char in special_characters:
        sc += 1
    else:
        n += 1
    

print("Number of vowels: ", vowels)
print("Number of consonants: ", consonants)
print("Number of special characters: ", sc)
print("Number of numbers: ", n)
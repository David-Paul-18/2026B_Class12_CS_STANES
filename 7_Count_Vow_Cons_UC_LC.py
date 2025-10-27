#Program 7 - COUNTING VOWELS, CONSONANTS, UPPER CASE & LOWER CASE CHARACTERS

file=open("Quotes.txt","w+")
file.write('''Where there is righteousness in the heart, there is beauty in the character.
When there is beauty in the character, there is harmony in the home.
When there is harmony in the home, there is an order in the nation.
When there is order in the nation, there is peace in the world.
- Dr. APJ ABDUL KALAM''')

file.seek(0)
data=file.read()
vowels=0
consonants=0
uppercs=0
lowercs=0
for letter in data:
    if letter.lower() in 'aeiou':
        vowels+=1
    if letter.lower() not in 'aeiou' and letter.isalpha():
        consonants+=1
    if letter.isupper():
        uppercs+=1
    if letter.islower():
        lowercs+=1
print(f"The no. of Vowels: {vowels}")
print(f"The no. of Consonants: {consonants}")
print(f"The no. of Upper Case letters: {uppercs}")
print(f"The no. of Lower Case letters: {lowercs}")
print(f"Total no. of Characters: {len(data)}")
file.close()